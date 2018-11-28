

    #include<bits/stdc++.h>
     
    #define X first
    #define Y second
    #define eb push_back
    #define pb pop_back
    #define siz(a) int(a.size())
    //for traversing the container (bcoz we cannot access linked list etc with direct index)
    //c stands for container and it for iterator
    #define tr(c, it) \
    		for(typeof(c.begin()) it=c.begin() ; it != c.end() ; it++)
    		
    #define all(c) c.begin(), c.end()
    #define present(container, element) (container.find(element) != container.end()) //whether the element is present in the container
     
    #define trace2(x, y)             cout <<#x<<": "<<x<<" | "<<#y<<": "<<y<< endl;
    #define trace3(x, y, z)          cout <<#x<<": "<<x<<" | "<<#y<<": "<<y<<" | "<<#z<<": "<<z<<endl;
    #define trace4(a, b, c, d)       cout <<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<endl;
    #define trace5(a, b, c, d, e)    cout <<#a<<": "<<a<<" | "<<#b<<": "<<b<<" | "<<#c<<": "<<c<<" | "<<#d<<": "<<d<<" | "<<#e<<": "<<e<<endl;
     
    #define scan(x) scanf("%lld", &x)
    #define print(x) printf("%lld ", x)
    #define pN printf("\n");
     
    using namespace std;
     
    typedef long long int ll;
    typedef vector < int > vi;
    typedef vector < vi > vvi;
    typedef vector < ll > vll;
    typedef vector < vll > vvll;
     
    typedef pair < ll , ll > pii;
    
 

const int MAX = 100005;
const ll INF = 1e14+1;
 

ll a[1001];
 
int main() {
	
	freopen("A-large(1).in","r",stdin);
	freopen("output.txt","w",stdout);
	
	
	
	ll i,j,k,t,ans,cnt,flag,y=0;
    
    cin>>t ;
    
    while(t--)
    {
		y++;
		string s;
		
		cin>>s;
		
		ll l=siz(s) ;
		
		for(i=0;i<l;i++)
		{
			if(s[i]=='+')
			{
				a[i]=1;
				//trace2(i,a[i]);
			}
			
			else
			{
				a[i]=0;
				
				
			}
		}
		
		cin>>k;
		
		for(i=0,ans=0;i<l;i++)
		{
			//trace2(a[8],a[8]);
			if(a[i]==0)
			{
				//trace3(i,a[i],ans) ;
				if(i+k>l)
				break ;
				
				//trace3(i,a[i],ans) ;
				for(j=i,cnt=0;cnt<k;j++,cnt++)
				{
					//trace2(j,a[j]) ;
					a[j]=a[j]^1 ;
					//trace2(j,a[j]) ;
				}
				ans++;
			}
		}
		
		for(i=0,flag=0;i<l;i++)
		{
			if(a[i]==0)
			flag=-1;
		}
		
		cout<<"Case #"<<y<<": " ;
		
		if(flag!=-1)
		cout<<ans<<endl;
		
		else
		cout<<"IMPOSSIBLE"<<endl ;
	}
}
