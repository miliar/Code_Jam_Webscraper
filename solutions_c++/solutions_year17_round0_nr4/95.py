#include <iostream>
#include <algorithm>
#include <limits>
#include <queue>

using namespace std;

bool bfs(int verts, int *graph, int s, int t, int *parent)
{
    bool *visited = new bool[verts];
    for(int i=0; i<verts; i++)
        visited[i] = false;

    queue<int> q;
    q.push(s);
    visited[s] = true;
    parent[s] = -1;
    while(!q.empty())
    {
        int u = q.front();
        q.pop();
        for(int v=0; v<verts; v++)
        {
            if(!visited[v] && graph[u*verts+v] > 0)
            {
                q.push(v);
                parent[v] = u;
                visited[v] = true;
            }
        }
    }

    return visited[t] == true;
}

void doCase()
{
    int n, m;
    cin >> n >> m;
    char *board = new char[n*n];
    for(int i=0; i<n*n; i++)
        board[i] = '.';
    for(int i=0; i<m; i++)
    {
        char m;
        int r, c;
        cin >> m >> r >> c;
        r--;
        c--;
        board[r*n+c] = m;
    }

    // set up newtwork:
    // nodes 0, 1: source and sink
    // nodes 2 -- 2n: (2 + i + j) diagonal i+j
    // nodes 2n + 1 -- 4n - 1: (3n + i - j) diagonal i-j
    // nodes 4n + 2 -- 5n - 1: (4n+i) rows i
    // nodes 5n + 2 -- 6n - 1: (5n+j) cols j

    int *graph = new int[6*n*6*n];
    for(int i=0; i<(6*n)*(6*n); i++)
    {
        graph[i] = 0;
    }
    for(int i=0; i<2*n-1; i++)
    {
        graph[0*(6*n) + 2+i] = 1;
        graph[(2*n+1+i)*(6*n) + 1] = 1;
    }
    for(int i=0; i<n; i++)
    {
        graph[0*(6*n) + 4*n+i] = 1;
        graph[(5*n+i)*(6*n) + 1] = 1;
    }

    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            int diag1 = 2+i+j;
            int diag2 = 3*n+i-j;
            if( (board[i*n+j] == 'o' || board[i*n+j] == '+') )
            {
                graph[diag1*(6*n) + diag2] = 0;
                graph[0*6*n + diag1] = 0;
                graph[6*n*diag2 + 1] = 0;
            }
            else
            {
                graph[diag1*(6*n) + diag2] = 1;
            }
            int row = 4*n+i;
            int col = 5*n+j;
            if( (board[i*n+j] == 'o' || board[i*n+j] == 'x') )
            {
                graph[row*(6*n) + col] = 0;
                graph[0*6*n + row] = 0;
                graph[6*n*col+1] = 0;
            }
            else
                graph[row*(6*n) + col] = 1;

        }
    }


//        for(int i=0; i<6*n; i++)
//        {
//            for(int j=0; j<6*n; j++)
//            {
//                cout << graph[i*(6*n)+j] << " ";
//            }
//            cout << endl;
//        }

    int *residual = new int[(6*n)*(6*n)];
    for(int i=0; i<6*n; i++)
        for(int j=0; j<6*n; j++)
            residual[i*(6*n)+j] = graph[i*(6*n)+j];
    int *parent = new int[6*n];

    while(bfs(6*n, residual, 0, 1, parent))
    {
        int flow = numeric_limits<int>::max();
        for(int v=1; v!=0; v=parent[v])
        {
            int u = parent[v];
            flow = std::min(flow, residual[u*(6*n)+v]);
        }
        for(int v=1; v!=0; v=parent[v])
        {
            int u = parent[v];
            residual[u*(6*n)+v] -= flow;
            residual[v*(6*n)+u] += flow;
        }
    }

    char *newboard = new char[n*n];
    int score = 0;
    int changed = 0;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            int diag1 = 2+i+j;
            int diag2 = 3*n+i-j;
            int row = 4*n+i;
            int col = 5*n+j;
            if(residual[diag1*(6*n)+diag2] == 0)
            {
                if(residual[row*(6*n)+col] == 0)
                {
                    newboard[i*n+j] = 'o';
                    score += 2;
                    if(board[i*n+j] != 'o')
                        changed++;
                }
                else
                {
                    newboard[i*n+j] = '+';
                    score += 1;
                    if(board[i*n+j] != '+')
                        changed++;
                }
            }
            else if(residual[row*(6*n)+col] == 0)
            {
                newboard[i*n+j] = 'x';
                score += 1;
                if(board[i*n+j] != 'x')
                    changed++;
            }
            else
                newboard[i*n+j] = '.';
        }
    }

    cout << score << " " << changed << endl;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            if(newboard[i*n+j] != board[i*n+j])
                cout << newboard[i*n+j] << " " << i+1 << " " << j+1 << endl;
        }
    }

    delete[] board;
    delete[] newboard;
    delete[] parent;
    delete[] graph;
    delete[] residual;
}

int main()
{
    int T;
    cin >> T;
    for(int i=0; i<T; i++)
    {
        cout << "Case #" << i+1 << ": ";
        doCase();
    }
}
