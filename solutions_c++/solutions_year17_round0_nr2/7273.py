#include<bits/stdc++.h>
using namespace std;
typedef long long lo;
typedef vector<string> vs;
typedef pair<lo,lo> ll;//pair
typedef vector<lo> vl;  //vector of long
typedef vector<ll > vll;   //vector of pair
typedef priority_queue<lo>p_q;
#define CHECK_BIT(var,pos) ((var) & (1<<(pos)))
#define X first
#define Y second
#define mp(a,b) make_pair((a),(b))
#define REP(a,b) for(lo i=(a);i<(b);i++)//no need to declare variable i
#define REPE(a,b,c,d) REP(a,b)for(lo j=(c);j<(d);j++)//no need to declare vaiables i,j
#define REPV(a,b,c) for((a)=b;(a)<(c);(a)++)//a is the variable
#define IREP(a,b) for(lo i=(a);i>=(b);i--)
#define IREPV(a,b,c) for((a)=b;(a)>=(c);(a)--)
#define all(v) (v).begin(),(v).end()
#define TRvl(c) for (vl::iterator it = (c).begin(); it != (c).end(); it++)
#define TRvll(c) for (vll::iterator it = (c).begin(); it != (c).end(); it++)
#define INF 2000000000
#define gc getchar_unlocked
#define pc putchar_unlocked
#define pb(a) push_back((a))
#define mod 1000000007

int main(){
    lo i,j,k,l,m,n,te,_,ans,t,a,b;
    bool flag;
    string s;
    ifstream fin ("B-large.in");
    ofstream fout ("bbans2.out");
    fin>>t;
    for(k=1;k<=t;k++){
        fin>>s;
        //fout<<s<<" ";
        l = s.length();
        IREP(l-1, 1){
            a=s[i]-'0';b=s[i-1]-'0';
            if(a==0){
                j = i;
                while(1){
                    if(s[j]-'0'==0){s[j]='9';for(n=j;n<l;n++)s[n]='9';}
                    else {s[j]=((s[j]-'0')-1)+'0';break;}
                    j--;
                }
                i = j+1;
                continue;
            }
            if(a < b){
                s[i]='9';for(n=i;n<l;n++)s[n]='9';
                s[i-1]=((s[i-1]-'0')-1)+'0';
            }
        }
        flag=false;
        fout<<"Case #"<<k<<": ";
        REP(0,s.length())if(flag)fout<<s[i];else{if(s[i]!='0'){fout<<s[i];flag=true;}}
        fout<<endl;
    }
}
