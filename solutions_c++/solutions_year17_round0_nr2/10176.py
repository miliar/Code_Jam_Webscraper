#include<bits/stdc++.h>
using namespace std ;
#define ll long long
#define  pb push_back
#define  mp make_pair
string ns(ll int n )
{
	 string t="" ;
	 while(n>0)
	 {
	 	int ld=n%10 ;
	 	char c=ld+'0';
	 	  t=t+c;
	 	  n=n/10 ;
	 }
	 reverse(t.begin(),t.end());
	 return t ;
}
string f(string s)
{
	 ll int l=s.length()-1,i,j ;
	 for(i=l-1;i>=0;i--)
	 {
	       int ni=s[i+1]-'0';
	       int ci=s[i]-'0';
	       if(ni<ci)
	       {
	       	     for(j=i+1;j<=l;j++)
	       	          s[j]=9+'0';
	       	      s[i]=ci-1+'0';  
		   }
	          
	 }
	 return s ;
}
ll int sn(string s)
{
	 ll int num =0,i;
	 for(i=0;i<s.length();i++)
	 {
	 	  num=num*10+s[i]-'0';
	 }
	 return num ;
}
int main()
{
//	freopen("i.in","r",stdin);
///freopen("o.out","w",stdout);
//	freopen(" i.txt",stdin);
  //  freopen("o.txt","w",stdout);
	int t ;
	cin>>t;
	while(t--)
	{
		  static int numm =1;
             ll  int n ;
               cin>>n ;
               string cns=ns(n) ;
            //   cout<<cns<<" ";
               string  fn=f(cns);
             //  cout<<fn<<"  ";
              ll  int an= sn(fn) ;
              cout<<"Case #"<<numm<<":"<<" "<<an<<endl ;
            //   cout<<an<<endl  ;
            numm++ ;
               
	}
	return 0;
}


