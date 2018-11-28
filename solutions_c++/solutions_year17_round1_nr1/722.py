#include<bits/stdc++.h>
#define ll long long
#define mp make_pair
#define vll vector<int>
#define pll pair<int, int>
#define pb push_back
#define cd complex<double>
#define x first
#define y second
using namespace std;
int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    ios_base::sync_with_stdio(false);
    int t,cases,r,c,i,j,k,l,n,m,o,ii,jj;
    cases=0;
    cin>>t;
    while(t--){
        cases++;
        cin>>r>>c;
        string s;
        int g[r][c];
        vll fil[26], col[26];
        for(i=0;i<r;i++){
            cin>>s;
            for(j=0;j<c;j++){
                g[i][j] = s[j];
                if(s[j]!='?'){
                    fil[s[j]-'A'].pb(i);
                    col[s[j]-'A'].pb(j);
                }
            }
        }
        for(k=0;k<26;k++){
            if(fil[k].size()>0){
                sort(fil[k].begin(), fil[k].end());
                sort(col[k].begin(), col[k].end());
                //cout<<k<<" "<<fil[k][0]<<" "<<fil[k].back()<<endl;
                for(i=fil[k][0];i<=fil[k].back();i++){
                    for(j=col[k][0];j<=col[k].back();j++){
                        g[i][j] = k+'A';
                    }
                }
            }
        }
        queue<pll> q;
        for(i=0;i<r;i++){
            for(j=0;j<c;j++){
                if(g[i][j]=='?')q.push(mp(i,j));
            }
        }
        while(!q.empty()){
            i=q.front().x;
            j=q.front().y;
            //cout<<i<<" "<<j<<endl;
            q.pop();
            if(g[i][j]!='?')continue;
            //cout<<i<<j<<endl;
            for(k=0;k<26;k++){
                if(fil[k].size()==0)continue;
                n = min(i, fil[k][0]);
                m = min(j, col[k][0]);
                l = max(i, fil[k].back());
                o = max(j, col[k].back());
                for(ii=n;ii<=l;ii++){
                    for(jj=m;jj<=o;jj++){
                        if(g[ii][jj]=='?' || g[ii][jj]==(k+'A'))continue;
                        break;
                    }
                    if(jj<=o)break;
                }
                if(ii<=l)continue;
                //cout<<k<<" "<<n<<" "<<m<<" "<<l<<" "<<o<<endl;
                for(ii=n;ii<=l;ii++){
                    for(jj=m;jj<=o;jj++){
                        g[ii][jj]=k+'A';
                    }
                }
                //cout<<k<<" "<<n<<" "<<m<<" "<<l<<" "<<o<<endl;
                fil[k][0] = n;
                col[k][0] = m;
                fil[k].pb(l);
                col[k].pb(o);
                break;
            }
        }
        cout<<"Case #"<<cases<<":\n";
        for(i=0;i<r;i++){
            for(j=0;j<c;j++)cout<<(char)g[i][j];
            cout<<"\n";
        }
    }
}
