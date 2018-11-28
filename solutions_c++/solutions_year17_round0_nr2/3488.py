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


bool check(int y){
	if(y<10) return true;
	string s=itos(y);
	int l=s.length();
	
	for(int i=0;i<l-1;i++) {
		if(s[i]>s[i+1]) return false;
	}
	return true;
}
int be[20];
 signed  main(){
int t;
 	cin>>t;
 	be[0]=1;
 	for(int i=1;i<=18;i++) be[i]=10*be[i-1];
 	
 	for(int qw=1;qw<=t;qw++){
 		int ans;
 		int n;
 		cin>>n;
 		if(check(n)) ans=n;
 		else{
 			int i=0;
 			while(check(n)==false){
 				int r=n/be[i];
 				r%=10;
 				if(r!=9){
 					n -= (r+1)*be[i];
 				}
 				
 				i++;
 			}
 			
 			ans=n;
 		}
 		
 		cout<<"Case #"<<qw<<": "<<ans<<endl;
 	}
 	
 //	cout<<i<<endl;
 	//  	printf("%.10f\n",ans[n-1]);
                    	return 0;
}