//If you want to get the logic visit my website codemaniac.tech
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#define MX 1000001
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define fs first
#define sec second
#define sc scanf
#define pr printf
typedef long long li;
using namespace std;
int main() {
	freopen("A-large.in","r",stdin);
	freopen("outputLA.in","w",stdout);
	int T,t;
	cin>>T;
    for(t=1;t<=T;++t){
    	int res=0;
       string s;
       int n,i,j,k;
       cin>>s;
       cin>>k;
       n=s.length();
       for(i=0;i<n;++i){
       	if(s[i]=='-'){
       		++res;
       		j=i;
       		if(j+k>n)
       			break;
       		else{
       			while(j<k+i){
       				if(s[j]=='-')
       					s[j]='+';
       				else
       					s[j]='-';
       				++j;
       			}
       		}
       	}
       }
       int flag=0;
       for(i=0;i<n;++i){
          if(s[i]=='-')
          {
          	flag=1;
          	break;
          }
       }
       if(flag==0)
          cout<<"Case #"<<t<<": "<<res<<endl;
      else
      	cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
    	 }
    	 return 0;
    	}