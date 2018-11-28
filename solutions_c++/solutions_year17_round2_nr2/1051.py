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
int r,o,y,g,b,v;
int n;
pa z[3];

void sh(){
	for(int i=0;i<3;i++) cout<<z[i].first<<" "<<z[i].second<<endl;
	cout<<endl;
	return;
}

 signed  main(){
cin>>T;
 	
 	
 	map<char,int> ma;
 	ma['R']=0;
 	ma['Y']=1;
 	ma['B']=2;
 	string h="RYB";
 	for(int qwe=1;qwe<=T;qwe++){
 		
 	cin>>n;
 		cin>>r>>o>>y>>g>>b>>v;
 	//	cout<<r<<y<<b<<endl;
 		string ans="";
 		if(n/2+1 <= r ||n/2+1 <= y ||n/2+1 <= b) {
 			ans="IMPOSSIBLE";
 			cout<<"Case #"<<qwe<<": "<<ans<<endl;
 			continue;
 		}
 		
 		int a[3];
 		a[0]=r,a[1]=y,a[2]=b;
 		
 		z[0]=mp(-r,0);
 		z[1]=mp(-y,1);
 		z[2]=mp(-b,2);
 	//	sh();
 		sort(z,z+3);
 		
 		if(z[0].second==0) ans += "R";
 		if(z[0].second==1) ans += "Y";
 		if(z[0].second==2) ans += "B";
 		z[0].first++;
 		for(int i=1;i<n;i++){
 			ans += " ";
 			sort(z,z+3);
 	//		sh();
 			if(z[0].second !=ma[ans[i-1]]) {
 				ans[i]= h[z[0].second];
 				z[0].first++;
 			}
 			else {
 				ans[i]= h[z[1].second];
 				z[1].first++;
 			}
 			
 		}
 		
 		
 		
 		cout<<"Case #"<<qwe<<": "<<ans<<endl;
 	}
 //	cout<<i<<endl;
 	//  	printf("%.10f\n",ans[n-1]);
                    	return 0;
}