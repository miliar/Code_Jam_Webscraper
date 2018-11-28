#include<bits/stdc++.h>
using namespace std ;
#define ll long long
#define  pb push_back
#define  mp make_pair
int main()
{
	ios_base::sync_with_stdio(false);
	int t ;
	cin>>t;
	set<ll int> s;
	set<ll int>::iterator j ;
	while(t--)
	{
		 static int tn=1;
        ll int n ,k,i,pi,fls,frs,mi ;
         cin>>n>>k  ;
         n=n+2 ;
         s.clear();
         s.insert(0);
         s.insert(n-1);
         while(k>0)
         {
         	  int om=-1 ,pc=-1; ;
         	  for(j=s.begin();j!=s.end();)
         	  {
         	  	    //cout<<"k"<<" ";
         	  	   ll  int fn=*j;
         	  	//   cout<<fn<<" ";
						j++ ;//s[i];
         	  	    ll int sn=*j;
         	  	  //   cout<<sn<<" ";
						//j--;//s[i+1];
         	  	    ll int mi=(fn+sn)/2 ;
         	  	  //   cout<<mi<<" ";
         	  	    ll int ls=mi-fn-1;
         	  	//     cout<<ls<<" ";
         	  	    ll int rs=sn-mi-1 ;
         	  	    ll int cm=min(ls,rs);
         	  	     if(cm>om)
         	  	     {
         	  	     	 //   cout<<"if"<<" ";
         	  	     	    om=cm ;
         	  	            pi=mi ;
							fls=ls ;
							frs=rs ; 
							pc=max(ls,rs);    	
				   	}
				   	else if(cm==om)
				   	{
				   	       int mc=max(ls,rs);
							  if(mc>pc)
							  {
							       pc=mc ;
								   pi=mi ;
								   fls=ls ;
								   frs=rs ;    	
							  }	
					}
				   	 j++ ;
				   	 if(j==s.end())
				   	   break ;
				   	 else
						j-- ;  
				  // 	if(j!=s.end())
				   //	    continue ;
				  // 	else 
					//   j-- ;  
			   }
			   //cout<<pi<<" nex "<<endl;
			   s.insert(pi);
			   k=k-1 ;
			 //  cout<<"next k"<<endl ;
		 }
		// cout<<fls<<" "<<frs<<" ";
		 cout<<"Case #"<<tn<<":"<<" "<<max(fls,frs)<<" "<<min(fls,frs)<<endl ;
		 tn++ ;
	}
	return 0;
}


