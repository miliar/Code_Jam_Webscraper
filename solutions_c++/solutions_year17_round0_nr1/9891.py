#include <bits/stdc++.h>

using namespace std;

#define INF 0x7fffffff
#define forstl(i,n) for(__typeof(n.begin())i = n.begin();i!=n.end();i++)
#define rforstl(i,n) for(__typeof(n.rbegin()) i = n.rbegin(); i!= n.rend(); i++)


typedef pair<int,int> ii;
typedef pair<int, ii> iii;
typedef priority_queue<ii> pqii;
typedef priority_queue<iii> pqiii;
typedef set<int> si;
typedef map<string, int> msi;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef unsigned long ull;
typedef long long ll;

int solve(string s, int k, set<string> ss, int lo, int dep)
{
    //cout << s << endl;
    if(!count(s.begin(), s.end(), '-')) return min(lo,dep);
    if(ss.find(s)!=ss.end()){
        return lo;
    }
    ss.insert(s);

    int sum = 0;
    bool ok = false;
    string nova = "";
    int ultimo = -1;
    for(int i=0; i<s.size(); i++)
    {
        if(s[i] == '-')
        {
            for(int j = max(i-(k-1), ultimo+1); j<=i; j++)
            {
                if((j+(k-1))<s.size())
                {
                    string a = string(s.begin(), s.begin()+j);
                    string b = string(s.begin()+(j+(k)),s.end());
                    string c = "";
                    for(int l = j; l<(j+k); l++)
                    {
                        c += s[l] == '+' ? '-' : '+';
                    }
                    cout << a << " " << c << " " << b << endl;
                    cout << a+c+b << endl;
                    //system("pause");
                    lo = min(lo, solve(a+c+b, k, ss, lo, dep+1));

                }
            }

            ultimo = i;
        }
    }

    return lo;
}

int solve2(string s, int k, set<string> ss, int lo, int dep)
{
    queue< pair<int, string> > q;
    q.push(make_pair(0,s));
    int qtd = count(s.begin(), s.end(), '-');

    while(!q.empty() && qtd)
    {
        pair<int, string> node;
        node = q.front(); q.pop();
        int ultimo = -1;
        for(int i=0; i<node.second.size(); i++)
        {
            if(node.second[i] == '-')
            {
                for(int j = max(i-(k-1), ultimo+1); j<=i; j++)
                {
                    if((j+(k-1))<node.second.size())
                    {
                        string a = string(node.second.begin(), node.second.begin()+j);
                        string b = string(node.second.begin()+(j+(k)), node.second.end());
                        string c = "";
                        for(int l = j; l<(j+k); l++)
                        {
                            c += node.second[l] == '+' ? '-' : '+';
                        }
                        //cout << i << " " << j << endl;
                        //cout << a << " " << c << " " << b << endl;
                        //cout << a+c+b << endl;
                        c = a+c+b;

                        int qtd = count(c.begin(), c.end(), '-');
                        if(!qtd) return node.first+1;

                        if(ss.find(c)==ss.end())
                        {
                            ss.insert(c);
                            q.push(make_pair(node.first+1,c));
                        }
                    }
                }

                ultimo = i;
            }
        }
    }

    return qtd == 0 ? 0 : INF;
}


int main()
{
    //code jam
    int t;
    int cases =1;
    int k, x;
    string s;

    while(scanf("%d", &t)!=EOF)
    {
        while(t--)
        {
            cin.ignore();
            set<string> ss;
            ss.clear();
            cin >> s >> k;
            x = solve2(s,k, ss, INF, 0);
            printf("Case #%d: ", cases++);
            if(x == INF) printf("IMPOSSIBLE\n");
            else printf("%d\n",x);
        }
    }
    return 0;
}


