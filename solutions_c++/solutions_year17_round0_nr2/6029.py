#include<bits/stdc++.h>
using namespace std;
#define MP          make_pair
#define PB          push_back
#define LL          long long
#define MAX         1000005
#define debug(a)    cout<<a<<"\n"
#define sd(a)       scanf("%d",&a)
#define sc(a)       scanf("%c",&a)
#define ss(a)       scanf("%s",&a)
#define mx(a,b,c)   max(a,max(b,c))
#define mn(a,b,c)   min(a,min(b,c))
#define pred(a)     printf("%0.6lf",a)
#define rep(i,x,b)  for(int i=x;i<b;i++)
#define rf          freopen("in.txt", "r", stdin)
#define wf          freopen("out.txt", "w", stdout)
#define fast()      ios_base::sync_with_stdio(0)
#define chloop(i,j) cout<<"i:"<<i<<" j:"<<j<<"\n"
#define sz(x)       x.size()
#define mst(x,a)    memset(x,a,sizeof(x))
#define pii         pair<LL,LL>
#define inf         1000000007
#define F            first;
#define S            second;    

const double eps=1e-9;
const double pi =acos(-1);
int a[10];
vector <int> v;
void correct()
{
 int x=-1;
  	for(int i=0;i<v.size()-1;i++)
  	{
  		if(v[i+1]>=v[i])
  		{
            
  		}
  		else
  		{
          x=i;break;
  		}

  	}
  	//debug("x:"<<x);
  	if(x!=-1)
  	{
  		v[x]--;
  		for(int i=x+1;i<v.size();i++)v[i]=9;
  	}
  return;

}
bool chk()
{
	for(int i=0;i<v.size()-1;i++)
	{
		if(v[i]>v[i+1])return false;
	}
	return true;
}
bool cmp(){}
LL t1,t2,t3,t4,t5;
int main()
{
   
  rf;
  wf;
 int t;
 cin>>t;
 for(int i1=0;i1<t;i1++)
 {
 	
 	int dig=0;
 	t3=0;

	  cin>>t1;
      cout<<"Case #"<<i1+1<<": ";
	  t2=t1;
	  while(t2)
	  {
	  	a[t2%10]++;
	  		v.PB(t2%10);
	  	t2/=10;
	  	dig++;

	  }
	
	  reverse(v.begin(),v.end());
	 
	 
	  if(t1<10)
	  {
	  	cout<<t1;
	  }
	  else{


	/*  for(int i=2;i<10;i++)
	  {
	  	 	
	  	if(a[i]>0){
	  		t3=1;
	  		break;
	  	}
	  }
	  if(!t3  && t1>9 )
	  {

	  	for(int i=0;i<dig-1;i++)cout<<9;

      } 
      */
 
  	while(!chk())
  	{
  		//cout<<"a";
  		correct();
  	}
  	for(int i=0;i<v.size();i++)
  		{
  			t4*=10;
  			t4+=v[i];

        }
        cout<<t4;
  /*	correct();
  	correct();
  	correct();
  	correct();
  	correct();
  	correct();
  	 for(int i=0;i<v.size();i++)
	  {
	  	cout<<v[i];
	  }*/

  

   }

    for(int i=0;i<10;i++)a[i]=0;
    	v.clear();
    t4=0;
    t2=0;
    t1=0;
    t3=0;
    debug("");

 }


}