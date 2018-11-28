#include <bits/stdc++.h>
using namespace std;

typedef vector<int> vi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef pair<int,ii> iii;
typedef vector<pair<ii,int>> viii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef map<int,int> mii;
typedef map<char,int> mci;
typedef priority_queue<int> pqi;
typedef priority_queue<ii> pqii;
typedef priority_queue<int,vi,greater<int>> pqmini;
typedef priority_queue<ii,vii,greater<ii>> pqminii;
typedef long long lli;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define si(n) scanf("%d",&n)
#define iout(n) printf("%d\n",n)
#define slli(n) scanf("%lld",&n)
#define lliout(n) printf("%lld\n",n)
#define FOR(i,n) for(int i=0;i<n;i++)

#define EPS 10e-9;
#define PI 3.14159265359
#define EULER 2.7182818284
#define MOD 1000000007

//global variables
//end global variables

void preprocess(void){
	return;
}

int main(void){
	//freopen("output.txt","w",stdout);
	//freopen("input.txt","r",stdin);
	preprocess();
	int t;
	si(t);
	//t=1;
	for(int z=1;z<=t;z++){
		printf("Case #%d: ",z);	
        char s[1007];
        scanf("%s",s);
        int k;
        si(k);
        int l=strlen(s);
        int ans=0;
        FOR(i,l-k+1){
            if(s[i]=='+'){
                continue;
            }
            ans++;
            FOR(j,k){
                if(s[i+j]=='+'){
                    s[i+j]='-';
                }
                else{
                    s[i+j]='+';
                }
            }
        }
        int flag=1;
        FOR(i,l){
            if(s[i]=='-'){
                flag=0;
                break;
            }
        }
        if(flag){
            iout(ans);
        }
        else{
            printf("IMPOSSIBLE\n");
        }
	}
	return 0;
}
