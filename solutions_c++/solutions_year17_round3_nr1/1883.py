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
         #define INF 1000000000
        #define scan(x) scanf("%llu", &x)
        #define print(x) printf("%llu ", x)
        #define pN printf("\n");
        #define  maxn 3.14159265358979323846 ;
         
        using namespace std;
         
        typedef  long long int ll;
        typedef unsigned long long ull ;
        typedef vector < int > vi;
        typedef vector < vi > vvi;
        typedef vector < ll > vll;
        typedef vector < vll > vvll;
         
        typedef pair < int , int > ii;
         
        const int mod=1e9+7;
        const int root=1e5+5;
        
      //  ll p[1001],s[1001];
        
       
       pair<ll,ll>a[1001];
       vector<pair<ll,ll> >dp ;
       vector<ll>ans;
        
       
        
        

ll modularExponentiation(ll x,ll n,ll M)
{
    ll result=1;
    while(n>0)
    {
        if(n % 2 ==1)
            result=(result * x)%M;
        x=(x*x)%M;
        n=n/2;
    }
    return result;
}



        
         
     
           
        int main()
        {
			freopen("A-large.in","r",stdin);
	        freopen("output.txt","w",stdout);
	
			
			ull t,n,k,i,j,cnt,sum,ans1,p=1;
			
			cin>>t;
			
			while(t--){
				
				cin>>n>>k;
				
				for(i=0;i<n;i++){
					cin>>a[i].X>>a[i].Y;
				}
				
				//sort(a,a+n);
				
				for(i=0;i<n;i++){
					
					dp.eb(make_pair(a[i].X*a[i].Y,a[i].X));
				}
				
				sort(dp.rbegin(),dp.rend());
				
				for(i=0,cnt=0,ans1=0;i<n;i++)
				{
					sum=dp[i].Y*dp[i].Y + 2*dp[i].X;
					
					for(j=0,cnt=1;cnt<k && j<n;j++){
							
							if(i!=j && dp[j].Y<=dp[i].Y)
							{
								sum=sum+2*dp[j].X ;
							//	trace5(i,j,dp[j].X,dp[i].Y,sum);
								cnt++;
								if(cnt==k)
								{
									ans1=max(ans1,sum);
									break;
								}
								
							}
						}
						//trace2(i,cnt);
						if(cnt==k)
						{ans1=max(ans1,sum);
						//trace2(i,ans1);
						}
							
							
							
					
					
					
					
					
				}
			
				
			
			
				
				
				
				
			 
				
				
				//trace2(ans1,i);
				
				double result=ans1*maxn; 
				
				cout << std::fixed;
                cout << std::setprecision(10);
                cout<<"Case"<<" #"<<p<<": " ;
                cout << result<<endl;
                p++;
                
                dp.clear();

			}
		}

