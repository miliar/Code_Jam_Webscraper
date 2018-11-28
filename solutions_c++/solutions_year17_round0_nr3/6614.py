#include<bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define SZ(v) (int)v.size()
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))
#define iter(it,s) for(__typeof(s.begin())it = s.begin();it!=s.end();it++)
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

const int OO = (int) 2e9;
const double eps = 1e-9;

// 1 based
int daysInMonths[] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };
#define Nd 0
#define Ed 1
#define Sd 2
#define Wd 3

using namespace std;

struct state
{
    int left, right;
    bool isEmpty;
    int maxLR;
    int minLR;
};


bool cmpmin(state a, state b)
{
    return a.minLR<=b.minLR;
}

bool cmpmax(pair<int, state> a, pair<int, state> b)
{
    return a.second.maxLR<=b.second.maxLR;
}

bool cmp(pair<int, state> a, pair<int, state> b)
{
    return a.first<b.first;
}


int main()
{

    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
#ifndef ONLINE_JUDGE
    freopen("C-small-1-attempt100.in", "rt", stdin);
    freopen("C-small-1-attempt100.out", "wt", stdout);
#endif

    int t, n, k, c=0;
    scanf("%d", &t);
    while(t--)
    {
        c++;
        scanf("%d %d", &n, &k);
        if(n==k)
        {
            printf("Case #%d: 0 0\n", c);
            continue;
        }
        vector<state> stall;

        vector<state>::iterator maxmin;
        vector<pair<int, state>>::iterator maxmax;

        FOR(i, 0, n)
        {
            stall.pb({0, 0, 1, 0, 0});
        }

        FOR(f, 0, k)
        {
            FOR(i, 0, n)
            {
                stall[i].left=0;
                stall[i].right=0;
                stall[i].maxLR=0;
                stall[i].minLR=0;
            }
            FOR(i, 0, n)
            {
                if(!stall[i].isEmpty)
                    continue;
                FOR(j, i+1, n)
                {
                    if(stall[j].isEmpty)
                        stall[i].right++;
                    else
                        break;
                }

                for(int j=i-1; j>=0; j--)
                {
                    if(stall[j].isEmpty)
                        stall[i].left++;
                    else
                        break;
                }
            }

            FOR(i, 0, n)
            {
                stall[i].maxLR = max(stall[i].right, stall[i].left);
                stall[i].minLR = min(stall[i].right, stall[i].left);
            }

            /*
            FOR(i, 0, n){
                    printf("left: %d, right: %d, maxLR: %d, minLR: %d\n", stall[i].left, stall[i].right, stall[i].maxLR, stall[i].minLR);
            }
            */
            maxmin = max_element(all(stall), cmpmin);
            vector<pair<int, state> > tab;
            tab.pb({maxmin - stall.begin(),*maxmin});
            //cout<<"maxmin : "<<maxmin - stall.begin()<<endl;
            FOR(i, 0, n)
            {
                if(stall[i].minLR == maxmin->minLR && stall[i].isEmpty)
                    tab.pb({i, stall[i]});
            }
           /* FOR(i, 0, SZ(tab))
            {
                printf("i : %d ,left: %d, right: %d, maxLR: %d, minLR: %d\n", tab[i].first, tab[i].second.left, tab[i].second.right, tab[i].second.maxLR, tab[i].second.minLR);
            }
            */
            if(tab.size()==1)
            {
                stall[tab[0].first].isEmpty=0;
            }
            else
            {
                maxmax = max_element(all(tab), cmpmax);
                //cout<<"maxmax : "<<maxmax->second.maxLR<<endl;
                vector<pair<int, state> >tab2;
                FOR(j, 0, SZ(tab))
                {
                    if(tab[j].second.maxLR == maxmax->second.maxLR)
                    {
                        tab2.pb({tab[j].first, maxmax->second});
                    }

                }
/*
                FOR(i, 0, SZ(tab2))
                {
                    printf("i : %d, left: %d, right: %d, maxLR: %d, minLR: %d\n",tab2[i].first, tab2[i].second.left, tab2[i].second.right, tab2[i].second.maxLR, tab2[i].second.minLR);
                }*/

                if(tab2.size()==1)
                {
                    stall[tab2[0].first].isEmpty=0;
                }
                else
                {
                    //cout<<min_element(all(tab2), cmp)->first<<endl;
                    stall[min_element(all(tab2), cmp)->first].isEmpty=0;
                }
            }
        }

        printf("Case #%d: %d %d\n", c,maxmax->second.maxLR, maxmin->minLR);

    }
    return 0;
}
