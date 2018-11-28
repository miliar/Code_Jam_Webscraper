#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
using namespace std;

typedef pair< int, int > ii;
//typedef pair< int, *int > piv;
const int INF = 0x3f3f3f3f;
const int MAX=100000;
const int MAXN = 1010;
string str;
int istate;
int ostate;
//piv state[MAX];
int k;

int flip(int s, int k, int i)
{
    for(int j=i; j<i+k; ++j)
    {
        s = s^(1 << j);
    }
    return s;
}

int* convert(int s, int size)
{
    int a[size];
    memset(a, 1, sizeof a);
    for(int i=0; i<size; ++i)
    {
        int t = s&(1 << (size-i));
        if(t==0) a[i] = 0;
    }
}

int bfs(int istate)
{
    queue<int> q;
    int d[MAX];
    memset(d, -1, sizeof d);

    d[istate] = 0;
    q.push(istate);

    while(!q.empty())
    {
		int u = q.front();
        q.pop();
        if(u == ostate){ break; }
		//for(int i=0; i< (int)str.size(); ++i)
        //{
        //    cout << convert(u, (int)str.size())[i];
        //}
        //cout << u << endl;
        for(int h=0; h < (int)str.size() - k + 1; ++h)
        {
            int newk = flip(u, k, h);

            if(d[newk] == -1)
            {
                //printf("ifpassed");
                d[newk] = d[u]+1;
            	q.push(newk);
			}
            else
            {
                //printf("newk = %d; d[newk] = %d; d[newk] +1 = %d\n", newk, d[newk], d[newk] +1);
            }
        }
    }

    return d[ostate];
}

int main()
{
    int t;
    cin >> t;
    for(int c=1; c<=t; ++c)
    {
        istate = 0;
        cin >> str;
        //cout << "flag1\n";
        int size = (int)str.size();
		//cout << size << endl;
        for(int i=0; i < size; ++i)
        {
            //istate[i] = (str[i]=='+' ? 1 : 0);
            if(str[size-i-1] == '+')
                istate |= (1 << i);
        }
        //printf("ss:%c\n", str[3]);
        //cout << istate;
        //states.push_back(make_pair(0, istate));
        ostate = (1 << (int)str.size() ) - 1;

        cin >> k;
        //cout << "flag2\n";
        int f = bfs(istate);
        if(f == -1) cout << "Case #" << c << ": " << "IMPOSSIBLE" << endl;
        else cout << "Case #" << c << ": " << f << endl;
    }

    return 0;
}
