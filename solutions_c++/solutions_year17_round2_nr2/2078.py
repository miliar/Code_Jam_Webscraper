#include <bits/stdc++.h>

using namespace std;

constexpr int MAX_N = 1000 + 2;

struct Node{
    int index;
    char color;
    char actualColor;
    
    bool operator < (const Node &X) const{
        return index < X.index;
    }
};

Node nodes[MAX_N];

bool isEdge(Node A, Node B){
    if (A.color & B.color)
        return false;
    else
        return true;
}

bool checkIfValid(int N){
    for (int i = 1; i + 1 <= N; i++)
        if (!isEdge(nodes[i], nodes[i + 1]))
            return false;
            
    if (!isEdge(nodes[1], nodes[N]))
        return false;
        
    return true;
}

int urm(int n, int N){
    if (n + 1 > N)
        return 1;
    else
        return n + 1;
}

int prec(int n, int N){
    if (n - 1 == 0)
        return N;
    else
        return n - 1;
}

void reverse_seq(int p, int q, int N){
    int prevP = p;
    vector<Node> tempNodes;
    
    do{
        tempNodes.push_back(nodes[p]);
        p = urm(p, N);
        
    } while (p != q);
    
    reverse(tempNodes.begin(), tempNodes.end());
    
    int k = 0;
    p = prevP;
    
    do{
        nodes[p] = tempNodes[k];
        p = urm(p, N);
        k++;
        
    } while (p != q);
}

void palmer(int N){
    int steps = N + 1;
    random_shuffle(nodes + 1, nodes + N + 1);
    
    while (steps > 0){
        steps--;
        
        int p = -1;
        int a = -1, b = -1;
        
        for (int i = 1; i + 1 <= N; i++)
            if (!isEdge(nodes[i], nodes[i + 1])){
                p = i;
                a = i;
                b = i + 1;
                break;
            }
            
        if (p == -1){
            if (!isEdge(nodes[N], nodes[1]))
                p = N,
                a = N,
                b = 1;
            else{
                break; // we are done
            }
        }
        
        assert(p != -1);
        int c = -1, d = -1;
        
        for (int j = 1; j + 1 <= N; j++){
            int j1 = j;
            int j2 = j + 1;
            
            set<int> Set{a, b, j1, j2};
            
            if (Set.size() == 4 && isEdge(nodes[a], nodes[j1]) && isEdge(nodes[j2], nodes[b])){
                c = j1;
                d = j2;
                break;
            }
        }
        
        if (c == -1 || d == -1){
            int j1 = N;
            int j2 = 1;
            
            set<int> Set{a, b, j1, j2};
            
            if (Set.size() == 4 && isEdge(nodes[a], nodes[j1]) && isEdge(nodes[j2], nodes[b])){
                c = j1;
                d = j2;
                break;
            }
        }
        
        if (c == -1 || d == -1){
            break;
        }
            
        reverse_seq(d, b, N);
    }
}

void solve_for_small(int N){
    sort(nodes + 1, nodes + N + 1);
    
    do{
        if (checkIfValid(N))
            break;
            
    } while (next_permutation(nodes + 1, nodes + N + 1));
}

int main()
{   
    assert(freopen("B-small-attempt1.in", "r", stdin));
    freopen("B-small-attempt1.out", "w", stdout);
    ios_base::sync_with_stdio(false);
    
    int TESTS;
    cin >> TESTS;
    
    for (int test = 1; test <= TESTS; test++){
        int N, R, O, Y, G, B, V;
        cin >> N >> R >> O >> Y >> G >> B >> V;
        
        /* R -> 0 => 1
         * Y -> 1 => 2
         * B -> 2 => 4
         * 
         * O -> (R, Y) => 1 | 2 => 3
         * G -> (Y, B) => 2 | 4 => 6
         * V -> (R, B) => 1 | 4 => 5
         */
        
        int indice = 0;
        
        while (R--){
            ++indice;
            nodes[indice] = {indice, 1, 'R'};
        }
        
        while (O--){
            ++indice;
            nodes[indice] = {indice, 1 | 2, 'O'};
        }
        
        while (Y--){
            ++indice;
            nodes[indice] = {indice, 2, 'Y'};
        }
        
        while (G--){
            ++indice;
            nodes[indice] = {indice, 2 | 4, 'G'};
        }
        
        while (B--){
            ++indice;
            nodes[indice] = {indice, 4, 'B'};
        }
        
        while (V--){
            ++indice;
            nodes[indice] = {indice, 1 | 4, 'V'};
        }
        
        assert(indice == N);
        
        if (N <= 9){
            solve_for_small(N);
        }
        else{
            int MAX_ITERS = 100;
        
            while (MAX_ITERS--){
                palmer(N);
                
                if (checkIfValid(N))
                    break;
            }
        }
        
        cout << "Case #" << test << ": ";
        
        if (checkIfValid(N)){
            for (int i = 1; i <= N; i++)
                cout << nodes[i].actualColor;
                
            cout << endl;
        }
        else
            cout << "IMPOSSIBLE" << endl;
    }
    
    return 0;
}