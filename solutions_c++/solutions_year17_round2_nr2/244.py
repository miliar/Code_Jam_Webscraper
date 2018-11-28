#include <iostream>
using namespace std;
int main(){
    int t;
    cin>>t;
    for (int l=0; l<t; ++l){
        int n, r, o, y, g, b, v;
        cin>>n>>r>>o>>y>>g>>b>>v;
        cout<<"Case #"<<l+1<<": ";
        if (v>=y && v>0){
            if (y==v && y+v==n){
                for (int i=0; i<n; ++i){
                    if (i%2){cout<<"Y";}
                    else {cout<<"V";}
                }cout<<endl;
            }
            else{cout<<"IMPOSSIBLE\n";}
            continue;
        }
        if (g>=r && g>0){
            if (r==g && r+g==n){
                for (int i=0; i<n; ++i){
                    if (i%2){cout<<"R";}
                    else {cout<<"G";}
                }cout<<endl;
            }
            else{cout<<"IMPOSSIBLE\n";}
            continue;
        }
        if (o>=b && o>0){
            if (b==o && b+o==n){
                for (int i=0; i<n; ++i){
                    if (i%2){cout<<"B";}
                    else {cout<<"O";}
                }cout<<endl;
            }
            else{cout<<"IMPOSSIBLE\n";}
            continue;
        }
        r-=g; y-=v; b-=o;
        n-=2*(g+v+o);
        int n1, n2, n3;
        char c1, c2, c3, d1, d2, d3;
        if (r>=y && r>=b){
            n1=r; n2=y; n3=b;
            c1='R'; c2='Y'; c3='B';
            d1='G'; d2='V'; d3='O';
        }
        else if (y>=r && y>=b){
            n1=y; n2=r; n3=b;
            c1='Y'; c2='R'; c3='B';
            d1='V'; d2='G'; d3='O';
        }else{
            n1=b; n2=r; n3=y;
            c1='B'; c2='R'; c3='Y';
            d1='O'; d2='G'; d3='V';
        }
        if (n1>n/2){cout<<"IMPOSSIBLE\n"; continue;}
        bool fn1=1, fn2=1, fn3=1;
        for (int i=0; i<n; ++i){
            if (n1>0 && i%2==0){
                cout<<c1;
                --n1;
                if (fn1){
                    int to;
                    if (d1=='G'){to=g;}
                    if (d1=='V'){to=v;}
                    if (d1=='O'){to=o;}
                    for(int i=0; i<to; ++i){
                        cout<<d1<<c1;
                    }
                }
                fn1=0;
            }else{
                if (n2>=n3){
                    cout<<c2;
                    --n2;
                    if (fn2){
                        int to;
                        if (d2=='G'){to=g;}
                        if (d2=='V'){to=v;}
                        if (d2=='O'){to=o;}
                        for(int i=0; i<to; ++i){
                            cout<<d2<<c2;
                        }
                    }
                    fn2=0;
                }else{
                    cout<<c3;
                    --n3;
                    if (fn3){
                        int to;
                        if (d3=='G'){to=g;}
                        if (d3=='V'){to=v;}
                        if (d3=='O'){to=o;}
                        for(int i=0; i<to; ++i){
                            cout<<d3<<c3;
                        }
                    }
                    fn3=0;
                }
            }
        }
        cout<<"\n";
    }
    return 0;
}
