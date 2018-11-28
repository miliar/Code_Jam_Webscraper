/*
ID: smfaisa1
LANG: C++
TASK: barn1
*/
#include <bits/stdc++.h>
using namespace std;
//////////////////Declarations/////////////////////
typedef vector<int> vi;
typedef vector<string> vs;
typedef map<string, vector<string> > ms;
typedef long long ll;
//////////////////Constants////////////////////////
#define PI acos(-1.0)
////////////////////IO/////////////////////////////
#define oi(x) printf("%d ",x)
#define oii(x,y) printf("%d %d ",x,y)
#define oiii(x,y,z) printf("%d %d %d ",x,y,z)
#define ol(x) printf("%lld ",x)
#define oll(x,y) printf("%lld %lld ",x,y)
#define olll(x,y,z) printf("%lld %lld %lld ",x,y,z)
#define od(x) printf("%lf ",x)
#define odd(x,y) printf("%lf %lf ",x,y)
#define oddd(x,y,z) printf("%lf %lf %lf ",x,y,z)

#define ln printf("\n")
#define sp printf(" ")
#define cas(x) printf("Case #%d:\n",x)

#define ini(x) scanf("%d",&x)
#define inii(x,y) scanf("%d %d",&x,&y)
#define iniii(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define ind(x) scanf("%lf",&x)
#define indd(x,y) scanf("%lf %lf",&x,&y)
#define inddd(x,y,z) scanf("%lf %lf %lf",&x,&y,&z)
#define inl(x) scanf("%lld",&x)
#define inll(x,y) scanf("%lld %lld",&x,&y)
#define inlll(x,y,z) scanf("%lld %lld %lld",&x,&y,&z)

#define FI(x) freopen(x,"r",stdin)
#define FO(x) freopen(x,"w",stdout)
//////////////////loops//////////////////////////////
#define go(i,n) for(int i=0; i<n; i++)
#define goo(i,k,n) for(int i=k; i<n; i++)
#define itr(i,arr,tp) for(tp :: iterator i = arr.begin(); i!=arr.end(); i++)
#define dump(arr,n) for(int i=0; i<n; i++) cout<<arr[i]<<endl;
#define dumpab(arr,a,b) for(int i=a; i<b; i++) cout<<arr[i]<<endl;
#define dump2(arr,row,col) for(int i=0; i<row; i++){for(int j=0; j<col; j++) oi(arr(i));ln;)}
//////////////////functions//////////////////////////
vector<string> split(string str, char delim=' ') {
    stringstream ss(str);
    string s;
    vector<string> v;
    while(getline(ss,s,delim)) v.push_back(s);
    return v;
}
long long s2i(string str, int base)
{
    return strtol(str.c_str(), 0, base);
}
/////////////////////////////////////////////////////////////////////////////////////////////////

int main()
{
    FI("in.txt");
    FO("out.txt");

    int T;
    cin>>T;
    go(tt,T)
    {
        int rr,cc;
        cin>>rr>>cc;
        string grid[rr+1],mask="";
        go(i,cc) mask+='?';
        go(i,rr) cin>>grid[i];
        set<char> ss;
        go(i,rr)
        {
            go(j,cc)
            {
                if(grid[i][j]=='?') continue;
                char c = grid[i][j];
                if(ss.find(c)!=ss.end()) continue;
                ss.insert(c);
                int l=j-1,r=j+1,u=i-1,d=i+1;
                while(l>=0 && grid[i][l]=='?') grid[i][l--]=c;
                while(r<cc && grid[i][r]=='?') grid[i][r++]=c;
                l++;r--;
                //go(iii,r) cout<<grid[iii]<<endl;cout<<endl;
                //cout<<grid[0]<<endl<<grid[1]<<endl<<grid[2]<<endl<<endl;
                //cout<<c<<" "<<l<<" "<<r<<endl;
                while(u>=0) {
                    bool flag = true;
                    for(int ii=l; ii<=r; ii++) {
                        if(grid[u][ii]!='?') {
                            flag = false;
                            break;
                        }
                    }
                    if(flag)
                        for(int ii=l; ii<=r; ii++) {
                            grid[u][ii]=c;
                        }
                    else break;
                    u--;
                }
                while(d<rr) {
                    bool flag = true;
                    for(int ii=l; ii<=r; ii++) {
                        if(grid[d][ii]!='?') {
                            flag = false;
                            break;
                        }
                    }
                    if(flag)
                        for(int ii=l; ii<=r; ii++) {
                            grid[d][ii]=c;
                        }
                    else break;
                    d++;
                }
            }
        }
        cas(tt+1);
        go(i,rr) cout<<grid[i]<<endl;
    }
    return 0;
}
