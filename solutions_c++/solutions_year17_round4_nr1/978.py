                            #include <bits/stdc++.h>
      //                      #include<iostream>
        //                    #include<cstdio>
          //                  #include<vector>
            //                #include<queue>
            //                #include<map>
              //              #include<cstring>
                            #include<string>
                            #include <math.h>
                            #include<algorithm>
                        //    #include <boost/multiprecision/cpp_int.hpp>
                            #include<functional>
             //        #define int long long
                            #define inf  1000000007
                            #define pa pair<int,int>
                            #define ll long long
                            #define pal pair<double,int>
                            #define ppa pair<string,pa>
                            #define ssa pair<string,int>
                            #define  mp make_pair
                            #define  pb push_back
                            #define EPS (1e-10)
                            #define equals(a,b) (fabs((a)-(b))<EPS)
                     
                           using namespace std;
              

                            //----------------kokomade tenpure------------


int T;

short int dp[711][711][711]={0};
bool dpp[1001][1001][1001]={0};

int dfs(int a1,int a2,int a3){
	if(a1<=710 &&a2<=710 &&a3<=710 )
	if(dpp[a1][a2][a3]==1) return dp[a1][a2][a3];
	int u=a1+a2+a3;
	
	if(u==0) return 0;
	int e=1;
	if(a1>=4){
		e=max(e,1+dfs(a1-4,a2,a3));
	} 
		if(a2>=2){
		e=max(e,1+dfs(a1,a2-2,a3));
	} 
		if(a3>=4){
		e=max(e,1+dfs(a1,a2,a3-4));
	} 
		if(a1>=1&& a3>=1){
		e=max(e,1+dfs(a1-1,a2,a3-1));
	} 
		if(a1>=2 && a2>=1){
		e=max(e,1+dfs(a1-2,a2-1,a3));
	} 
		if(a3>=2 && a2>=1){
		e=max(e,1+dfs(a1,a2-1,a3-2));
	} 
 
if(a1<=710 &&a2<=710 &&a3<=710 )
	{dpp[a1][a2][a3]=1;
	dp[a1][a2][a3]=e;
	}
	return e;
}


double pi=3.14159265358979323846264;
int n,k;
 signed  main(){
 std::cin>>T;
 	
 	
 	dp[0][0][0]=0;
 	dpp[0][0][0]=1;
 	dfs(1000,0,0);
 	dfs(0,1000,0);
 	dfs(0,0,1000);
 	dfs(710,710,710);
 	
 	for(int qwe=1;qwe<=T;qwe++){
 		int a[10]={0};
 		int p;
 		std::cin>>n>>p;
 		for(int i=0;i<n;i++){
 			int u;
 			std::cin>>u;
 			a[u%p]++;
 		}
 		int ans=0;
 		if(p==2){
 			ans =a[0];
 			if(a[1]>0)ans += 1+ (a[1]-1)/2;
 			
 			
 		}
 		if(p==3){
 			ans=a[0];
 		int	r=std::min(a[1],a[2]);
 			ans += r;
 			a[1]-=r;
 			a[2]-=r;
 			if(a[1]>0) ans += 1+(a[1]-1)/3;
 			else if(a[2]>0) ans += 1+(a[2]-1)/3;
 		}
 		if(p==4){
 			ans=a[0]+dfs(a[1],a[2],a[3]);
 			
 		}
	
 		std::cout<<"Case #"<<qwe<<": "<<ans<<std::endl;
// 		printf("%d\n",ans);
 	}
 //	cout<<i<<endl;
 	//  	printf("%.10f\n",ans[n-1]);
                    	return 0;
}