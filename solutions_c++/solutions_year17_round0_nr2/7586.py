
/* 
 #        "    ""#    ""#                      #        
 #   m  mmm      #      #     mmm    mmm    mmm#   mmm  
 # m"     #      #      #    #"  "  #" "#  #" "#  #"  # 
 #"#      #      #      #    #      #   #  #   #  #"""" 
 #  "m  mm#mm    "mm    "mm  "#mm"  "#m#"  "#m##  "#mm"  */


#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef pair<int,int> pii;
typedef long long ll;
typedef double ld;
typedef vector<int> vi;
#define fi first
#define se second
#define fe first
#define SZ 666666
#define si(n) scanf("%d",&n);
#define sl(n) scanf("%ld",&n);
#define pi(n) printf("%d\n",n);
#define pl(n) printf("%ld\n",n);
#define pf(n) printf("%f\n",n);
#define FILL(a,b) memset(a,0,sizeof(b));
#define rep(i,n) for(int i=0;i<n;i++)
#define reps(i,a,b) for(int i=1;i<=b;i++)
const int INF=1e9+5;
const int MOD=1000000007;

//--------------**************---------------------

bool isPrime(int n){
    if(n<=1)    return false;
    if(n<=3)    return true;
    if(!(n%2) or !(n%3))   return false;
    for(int i=5;i*i<=n;i+=6){
        if(!(n%i) or !(n%(i+2)))  return false;
    }
    return true;
}

int main()
{
	int t;
	cin>>t;
	for(int j=1;j<=t;j++)
	{
	string s;
	cin>>s;
	int n=s.length();
	string ans="";
	int ind=-1;
	int len=s.length()-1;
	bool flag=false;
	for(int i=0;i<n-1;i++)
	{
		if(s[i]>s[i+1])flag=true;
	}
	if(!flag){
		cout<<"Case #"<<j<<": "<<s<<endl; continue;
	}
	for(int i=0;i<s.length()-1;i++)
	{
		if(s[i]>=s[i+1]){ind=i;  break;}
	}
	if(ind==-1){
		cout<<"Case #"<<j<<": "<<s<<endl; continue;
	}
	if(s[ind]=='1' && ind==0){
		string ans1="";
		for(int i=0;i<n-1;i++ )
		{
			ans1=ans1+'9';
		}
		cout<<"Case #"<<j<<": "<<ans1<<endl; continue;
	}
	else{
     //cout<<"Casa "<<endl;
          for(int i=0;i<ind;i++)ans=ans+s[i];
         // 	cout<<ans<<" "<<ind<<endl;
          	char c=s[ind];
           if(c=='1')ans=ans+'9';
           else c--;
           ans=ans+(c);
           for(int i=ind+1;i<n;i++)ans=ans+'9';
         	cout<<"Case #"<<j<<": "<<ans<<endl;
	}

	}
}
