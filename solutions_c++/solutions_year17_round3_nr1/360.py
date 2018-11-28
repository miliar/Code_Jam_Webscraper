                            #include <bits/stdc++.h>
                            #include<iostream>
                            #include<cstdio>
                            #include<vector>
                            #include<queue>
                            #include<map>
                            #include<cstring>
                            #include<string>
                            #include <math.h>
                            #include<algorithm>
                        //    #include <boost/multiprecision/cpp_int.hpp>
                            #include<functional>
                     #define int long long
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
                     //priority_queue<int, vector<int>, greater<int> > que;
                            class Point{
                            	public:
                            	double x,y;
                            	Point(double x=0,double y=0):x(x),y(y) {}
                            	Point operator + (Point p) {return Point(x+p.x,y+p.y);}
                            	Point operator - (Point p) {return Point(x-p.x,y-p.y);}
                            	Point operator * (double a) {return Point(x*a,y*a);}
                            	Point operator / (double a) {return Point(x/a,y/a);}
                            	double absv() {return sqrt(norm());}
                            	double norm() {return x*x+y*y;}
                            	bool operator < (const Point &p) const{
                            		return x != p.x ? x<p.x: y<p.y;
                            	}
                            	bool operator == (const Point &p) const{
                            		return fabs(x-p.x)<EPS && fabs(y-p.y)<EPS;
                            	}
                            };
                            typedef Point Vector;
                     
                            struct Segment{
                            Point p1,p2;
                            };
                     
                        double hen(Vector a){
                        if(fabs(a.x)<EPS && a.y>0) return acos(0);
                        else if(fabs(a.x)<EPS && a.y<0) return 3*acos(0);
                        else if(fabs(a.y)<EPS && a.x<0) return 2*acos(0);
                        else if(fabs(a.y)<EPS && a.x>0) return 0.0;
                        else if(a.y>0) return acos(a.x/a.absv());
                        else return 2*acos(0)+acos(-a.x/a.absv());
                     
                        }
                     
                string itos( int i ) {
                ostringstream s ;
                s << i ;
                return s.str() ;
                }
                 
                int gcd(int v,int b){
                	if(v>b) return gcd(b,v);
                	if(v==b) return b;
                	if(b%v==0) return v;
                	return gcd(v,b%v);
                }
                            double dot(Vector a,Vector b){
                            	return a.x*b.x+a.y*b.y;
                            }
                            double cross(Vector a,Vector b){
                            	return a.x*b.y-a.y*b.x;
                            }
                        
                double distans(double x1,double y1,double x2,double y2){
                	double rr=(x1-x2)*(x1-x2)+(y1-y2)*(y1-y2);
                	return sqrt(rr);
                	
                }

                            //----------------kokomade tenpure------------


int T;

double pi=3.14159265358979323846264;
int n,k;
 signed  main(){
cin>>T;
 	
 	
 	
 	
 	for(int qwe=1;qwe<=T;qwe++){
 		cin>>n>>k;
 		pa p[1010];
 		vector<double> ve;
 		for(int i=0;i<n;i++)cin>>p[i].first>>p[i].second;
 		double ans=0.0;
 		for(int i=0;i<n;i++){
 			ve.clear();
 			
 			for(int j=0;j<n;j++){
 				if(i==j) continue;
 				if(p[j].first>p[i].first) continue;
 				ve.pb(-2.0*(p[j].first+0.0)*pi*(0.0+p[j].second));
 			}
 			if(ve.size()<k-1) continue;
 			
 			sort(ve.begin(),ve.end());
 			double we=0.0;
 			for(int j=0;j<k-1;j++) we -= ve[j];
 			we += (p[i].first+0.0)*(p[i].first+0.0)*pi+2.0*(p[i].first+0.0)*pi*(0.0+p[i].second);
 			
 			ans=max(ans,we);
 			
 		}
 		
 		
 		

 		cout<<"Case #"<<qwe<<": ";
 		printf("%.10f\n",ans);
 	}
 //	cout<<i<<endl;
 	//  	printf("%.10f\n",ans[n-1]);
                    	return 0;
}