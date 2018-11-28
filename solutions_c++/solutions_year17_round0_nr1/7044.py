#include<bits/stdc++.h>
#define lli long long int
#define pi pair<int,int>
#define plli pair<lli,lli>
#define m_p make_pair
#define vi vector<int>
#define vlli vector<lli>
#define vc vector<char>
#define si set<int>
#define slli set<lli>
#define stklli stack<lli>	//push - pop
#define qulli queue<lli>	//push - pop
#define listlli	list<lli>	//push_back/front() pop_back/front()
#define p_qdec priority_queue< lli , vector < lli > > //for decreasing 5,3,2
struct compare{

	bool operator()(const lli& l,const lli& r){

		return l>r;

	}

};
#define p_qinc priority_queue< lli , vector < lli > ,compare>	//increasing order 0,1,2,3

#define ff(i,a,b) for(i=a;i<b;i++)
#define fb(i,a,b) for(i=a;i>=b;i--)
#define pb push_back
#define c(a) cin>>a
#define o(a) cout<<a<<endl
#define sf(a) scanf("%d",&a)
#define pf(a) printf("%d\n",a)
using namespace std;
/*
int *ptr;
ptr = (int*) malloc(num * sizeof(int));
memset(arr,0, sizeof(arr)); //only for zero value
free(ptr);
*/
int main(int argc, char const *argv[])
{
  int t,n,k,i,f,j=1;
  sf(t);
  string s;

  while(t-->0){
      cin>>s;
      sf(k);
      f=1;
      n=s.size();
      int b[n+1]={0};
      int ans=0;
      int ct=0;
      ff(i,0,n){
        ct+=b[i];
        //cout<<ct<<endl;
        if(s[i]=='+'&&ct%2==1){
          if(i+k-1>=n){
            cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
            f=0;
            break;
          }else{
            b[i+k]--;
            ct++;
            ans++;
          }
        }else if(s[i]=='-'&&ct%2==0){
          if(i+k-1>=n){
            f=0;
            cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
            break;
          }else{
            b[i+k]--;
            ct++;
            ans++;
          }
        }
      }
      if(f) cout<<"Case #"<<j<<": "<<ans<<endl;
      j++;
  }
	return 0;
}
