#pragma GCC optimize "Ofast,omit-frame-pointer,inline"
#include <bits/stdc++.h>
using namespace std;

long double PI = 3.14159265358979323846264338327950288;
long double dp[1005][1005];
long double INF = 1e18;
int n;
vector<int> radii, height;

long double getSideArea(long double height, long double radius){
    return 2*PI*radius*height;
}

long double circleArea(long double radius){
    return PI*radius*radius;
}

long double getDiffArea(long double topRadius, long double bottomRadius){
    long double areaBelow = circleArea(bottomRadius);
    long double areaAbove = circleArea(topRadius);
    return areaBelow - areaAbove;
}


long double findMax(int prev, int k){
    if(k==0)
        return 0;
    
    if(dp[prev][k] != -INF){
        return dp[prev][k];
    }

    long double maxx = -INF;

    for(int i= prev+1; i<n; i++){
        //choose i
        long double chooseArea = getSideArea(radii[i], height[i]) + getDiffArea(radii[prev],radii[i]);
        maxx = max(maxx, chooseArea+findMax(i,k-1));
    }
    return dp[prev][k] = maxx;
}

void cls(){
    int i,j;
    for(i=0;i<1005;i++)
        for(j=0;j<1005;j++)
            dp[i][j]=-INF;
}


int main(){
    ios::sync_with_stdio(false);
    freopen("gcj1input2.in","r",stdin);
    freopen("output1_large.txt","w",stdout);
    long long t,i,c=1,k,x,y;
    vector<pair<int,int>> pairs;
    cin>>t;
    while(t--){
        radii.clear();
        height.clear();
        pairs.clear();
        cls();
        cin>>n>>k;        
        for(i=0;i<n;i++){
            cin>>x;
            cin>>y;
            pairs.push_back(make_pair(x,y));
        }
        sort(pairs.begin(),pairs.end());
        for(i=0;i<n;i++){
            radii.push_back(pairs[i].first);
            height.push_back(pairs[i].second);   
        }         

        long double ans = -INF;
        for(i=0;i<n;i++){
            ans = max(ans, circleArea(radii[i])+getSideArea(radii[i], height[i])+findMax(i,k-1));
        }

    	cout<<"Case #"<<c++<<": "<<std::fixed<<std::setprecision(12)<<ans<<endl;
    }
	return 0;
}