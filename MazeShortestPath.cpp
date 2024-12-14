#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

struct Point {
    int x, y, distance;
    Point(int x, int y, int distance) : x(x), y(y), distance(distance) {}
};

bool isValid(int x, int y, int N, vector<vector<int> >& maze, vector<vector<bool> >& visited) {
    return (x >= 0 && x < N && y >= 0 && y < N && maze[x][y] == 1 && !visited[x][y]);
}

int shortestPath(vector<vector<int> >& maze, int N) {
    if (maze[0][0] == 0 || maze[N - 1][N - 1] == 0) {
        return 0;
    }

    vector<vector<bool> > visited(N, vector<bool>(N, false));
    queue<Point> q;
    int rowDir[] = {-1, 1, 0, 0};
    int colDir[] = {0, 0, -1, 1};

    q.push(Point(0, 0, 1));
    visited[0][0] = true;

    while (!q.empty()) {
        Point p = q.front();
        q.pop();

        if (p.x == N - 1 && p.y == N - 1) {
            return p.distance;
        }

        for (int i = 0; i < 4; i++) {
            int newX = p.x + rowDir[i];
            int newY = p.y + colDir[i];

            if (isValid(newX, newY, N, maze, visited)) {
                visited[newX][newY] = true;
                q.push(Point(newX, newY, p.distance + 1));
            }
        }
    }

    return 0;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <filename>" << endl;
        return 1;
    }

    ifstream inputFile(argv[1]);
    if (!inputFile) {
        cerr << "Error opening file: " << argv[1] << endl;
        return 1;
    }

    vector<vector<int> > maze;
    string line;
    while (getline(inputFile, line)) {
        vector<int> row;
        for (size_t i = 0; i < line.length(); ++i) {
            char ch = line[i];
            if (ch == '0' || ch == '1') {
                row.push_back(ch - '0');
            }
        }
        maze.push_back(row);
    }

    inputFile.close();

    int N = maze.size();
    int result = shortestPath(maze, N);
    cout << result << endl;

    return 0;
}
/*
 ₊      ・      ₊               ₊            °        ☆
      ☆    ₊          ⋆.       ₊        ★           ⊹
               ⟡     ⊹             .                     ☾
  ⋆      .                  ⟡      .         ₊         .
                    ˖                   ˖           °
 ☾     ｡   ∩―――――∩  ₊        ⊹         ☆
             || ∧,,∧ ∧,,,∧     ||       .            ⋆
     .  ⋆   ||(˶´ ｰ(˶-ω-˶)   ||  𝓂𝓌𝒶 💖       ₊
   ☆      |ﾉ￣づ⌒⌒￣  ＼     ⋆         .
 .      .    (　ノ　⌒⌒ ヽ   ＼      ₊         ☾
       ₊     ＼   ノ||￣￣￣￣￣||         ₊
 　             ＼,ﾉ||￣￣￣￣￣||
 */
