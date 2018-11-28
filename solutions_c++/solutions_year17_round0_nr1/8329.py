#include <iostream>
#include <cstdio>
#include <set>
#include <queue>

#define INFINITO 1000000

using namespace std;

set <string> s;

int faster(string& S, int K, int times, int tam)
{
    queue < pair <string, int> > q;

    q.push(make_pair(S,0));

    while (!q.empty())
    {
        pair <string, int> p = q.front();
        q.pop();
        S = p.first;
        int T = p.second;
        if (s.count(S) == 0)
        {
            s.insert(S);
            int i, j;
            bool happy = true;
            for (i = 0; i < tam; i++)
            {
                if (S[i] == '-')
                {
                    happy = false;
                    break;
                }
            }
            if (happy)
                return T;
            string aux;
            for (i = 0; i <= tam-K; i++)
            {
                aux = S;
                for (j = i; j < i+K; j++)
                {
                    aux[j] = (aux[j] == '+' ? '-' : '+');
                }
                if (s.count(aux) == 0)
                {
                    q.push(make_pair(aux,T+1));
                }
            }
        }
    }
    return -1;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        string S;
        int K;
        cin >> S >> K;
        int times = faster(S,K,0,S.size());
        cout << "Case #" << i+1 << ": ";
        if (times == -1)
            cout << "IMPOSSIBLE";
        else
            cout << times;
        cout << endl;
        s.clear();
    }
    return 0;
}
