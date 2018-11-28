#include <bits/stdc++.h>
using namespace std;

double PI = 3.14159265358979323846 ;

vector<pair<double , double> > arr , radii ;
vector<double> area ;

//bool visited[1000] ;

double max_area = -1 ;
int cons_k ;

double get(double r , double h){
    return (PI*r*r + 2*PI*r*h) ;
}

bool cmp(pair<double,  double> i , pair<double,  double> j){
	if(i.first == j.first) return i.second < j.second ;
	else return i.first < j.first ;
}

double get_ans(int i ,int k){
	if(i == -1 || k == -1) return 0 ;
	if(k > i) return 0 ;
	
	if(k != cons_k)
	return max( get_ans(i-1 , k-1) + 2*PI*arr[i].first*arr[i].second , get_ans(i-1,k) ) ;
	
	else return max(get_ans(i-1,k-1)+2*PI*arr[i].first*arr[i].second + PI*arr[i].first*arr[i].first, get_ans(i-1,k) ) ;
}

int main()
{
    int t ;
    cin>>t ;
    for(int tc = 1 ; tc <= t ; tc++){
        int n , k ;
        cin>>n>>k ;
        
        max_area = -1 ;
        
        int id[n] ;
        double r , h ;
        
        arr = vector<pair<double , double> >(n , make_pair(0,0)) ;
        //radii = vector<pair<double , double> >(n , make_pair(0,0)) ;
        area = vector<double>(n) ;
        
        for(int i = 0 ; i < n ; i++){
            cin>>r>>h ;
            arr[i] = (make_pair(r,h));
            //radii[i] = make_pair(r,i) ;
            area[i] = (get(r,h));
            id[i] = i ;
            max_area = max(area[i] , max_area) ;
        }
        
        cons_k = k-1 ;
        sort(arr.begin() , arr.end() , cmp) ;
        
        r = 0 ;
        double ans = 0 ;
        
       ans = get_ans(n-1 , k-1);
        
       printf("Case #%d: %0.8lf\n" , tc , ans) ;
    }
    return 0;
}

