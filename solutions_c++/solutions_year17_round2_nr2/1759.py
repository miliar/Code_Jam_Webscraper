#include <bits/stdc++.h>
#define SC(n) scanf("%d",&n);
#define PR(n) cout << n ;
#define endl "\n"
using namespace std;
typedef unsigned long long int ull;

int g[6][6]= {{1,1,0,0,0,1},{1,1,1,0,0,0},{0,1,1,1,0,0},{0,0,1,1,1,0},{0,0,0,1,1,1},{1,0,0,0,1,1}};
char cl[] = {'R','O','Y','G','B','V'};
int C[6];
int n;
void pc()
{
    for(int i=0;i<6;i++)
        cout << C[i] << " ";
    cout << "\n";
}
string ans;
int dfs(int s, string tmp)
{
    //cout << tmp << endl;
    if(tmp.length() == n && tmp[0]!=tmp[tmp.length()-1])
    {
        ans = tmp;
      //  cout << "success" << endl;
        return 1;
    }

    int mx = 0,mxi=-1;

    for(int i=0;i<6;i++)
    {
        if(g[s][i] == 0 && C[i] > 0)
        {
            if(C[i] > mx){
                mxi = i;
                mx = C[i];
            }
        }
    }
    //cout << mxi << endl;
    if(mxi != -1){
        C[mxi]--;
        return dfs(mxi,tmp+cl[mxi]);
    }
    else
    return 0;

}


void solve(int tc)
{
    cout << "Case #"<< tc<<": ";
    int a;
    int k=0;

    cin >> n;
    string s = "";
    ans = "";
    for(int i=0;i<6;i++)
        C[i] = 0;

    for(int i=0;i<6;i++){
        cin >> a;
        C[i] = a;
    }
    //cout << s << endl;
    string tmp = "";
    for(int i=0;i<6;i++){
        if(C[i] != 0){
            C[i]--;
            tmp += cl[i];
            k = dfs(i,tmp);
            if(k == 1){ break;}
            C[i]++;
        }
    }
    //cout << k << endl;
    if(k==1)
        cout << ans << endl;
    else
        cout << "IMPOSSIBLE" << endl;

}


int main(void)
{
    int tc=1,T;
    cin >> T;
    while(T--)
        solve(tc++);
    return 0;
}
