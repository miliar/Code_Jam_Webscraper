

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
 


 
int main() {
 
 
	ll t,i,flag,x,j,y=0;	
	
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
		
    cin>>t ;
    
    while(t--)
    {
		y++;
		string s;
		
		cin>>s;
		
		ll l=siz(s);
		
		for(i=0,flag=0;i<l-1;i++)
		{
			if(s[i]>s[i+1])
			{
				x=i;
				flag=-1;
				break;
			}
		
		}
		if(flag==-1)
		{
			while(i>=0 && s[i]==s[x])
			{
				i--;
			}
			
			i++;
			
			x=s[i]-'0' ;
			x--;
			s[i]=x+'0' ;
			
			cout<<"Case #"<<y<<": " ;
			for(j=0,flag=0;j<l;j++)
			{
				if(j>i)
				s[j]='9' ;
				
				if(flag==0 && s[j]=='0')
				continue;
				
				else{
				cout<<s[j];
				flag=-1;
			}
			}
			
			cout<<endl;
		}
		else{
			cout<<"Case #"<<y<<": " ;
		for(i=0;i<l;i++)
		{
			//if(s[i]!='0')
			
			cout<<s[i] ;
		}
		
		cout<<endl;
	}
		
		
	}
}
