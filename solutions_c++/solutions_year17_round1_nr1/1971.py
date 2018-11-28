#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
#define mp make_pair
#define first fi
#define second se

#define DEBUG 1
#define debug(x) if(DEBUG) cout << x << '\n'

#define MAX 100001

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for(int case_no = 1; case_no <= T; case_no++)
    {
        int N, M;
        cin >> N >> M;
        string G[26];
        for(int i = 0; i < N; i++)
            cin >> G[i];
        int R[26] = {0};
        for(int i = 0; i < N; i++)
        {
            bool nochar = true;
            int p = -1, q = -1;
            char fchar = G[i][0];
            bool change = false;
            for(int j = 0; j < (int)G[i].length(); j++)
            {
                if (G[i][j] != '?')
                {
                    q = j;
                    fchar = G[i][j];
                    nochar = false;
                    if (change)
                    {
                        change = false;
                        for(int k = p; k <= q-1; k++)
                            G[i][k] = fchar;
                        p = j;
                    }
                }
                else
                {
                    if (!change)
                    {
                        p = j;
                        change = true;
                    }    
                }
            }
            if (change && !nochar)
            {
                for(int k = p; k < M; k++)
                    G[i][k] = fchar;
            }
            if (nochar)
                R[i] = 1;
        }
        int s = -1;
        int e = -1;
        bool rem = true;
        for(int i = 0; i < N; i++)
            if (R[i] && rem)
            {
                s = i;
                rem = 0;
            }
            else
            {
                if (!rem && !R[i])
                {
                    for(int j = s; j < i; j++)
                        G[j] = G[i];
                    rem = 1;
                    e = i;
                }
                else if (!R[i])
                    e = i;
            }
        if (!rem)
        {
            for(int j = s; j < N; j++)
                G[j] = G[e];
        }
        printf("Case #%d:\n", case_no);
        for(int i = 0; i < N; i++)
            cout << G[i] << endl;
    }
    return 0;
}
