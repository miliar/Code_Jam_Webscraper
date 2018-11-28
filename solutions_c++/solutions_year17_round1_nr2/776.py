#include<iostream>
#include<string>
#include<map>
#include<vector>
using namespace std;
typedef pair<string, string> Pair;
//bool compare(Pair x,Pair y){
//    if(x.first==y.first)
//        return x.second<y.second;
//    return x.first<y.first;
//}
bool comp(long long int qx,long long int qy,long long int nx,long long int ny){
    //qx/nx< qy/ny
    return qx*ny<qy*nx;
}
//bool check(long long int qx,long long int qy,long long int nx,long long int ny){
//    if(!compare(qx,qy,nx,ny)){
//        long long int tmp=qx;
//        qx=qy;
//        qy=tmp;
//        tmp=nx;
//        nx=ny;
//        ny=tmp;
//    }
//}
int main(){
    int TT;
    cin>>TT;
    int n;
    int p;
    int r[2000]={0};
    int q[100][200];
    int a[2000]={0};
    for(int T=1;T<=TT;++T){
        cin>>n>>p;
        for(int i=0;i<n;++i){
            cin>>r[i];
        }
        for(int i=0;i<n;++i){
            for(int j=0;j<p;++j){
                cin>>q[i][j];
            }
            sort(&(q[i][0]),&(q[i][p]));
        }
        for(int i=0;i<n;++i)
            a[i]=0;

        int mi=0;
        bool keep=true;
        int counter=0;
        while(keep){
            //find min
            mi=0;
            for(int i=1;i<n;++i){
                if(comp(q[i][a[i]],q[mi][a[mi]],r[i],r[mi])){
                    mi=i;
                }
            }
            //check if fit in range
            long long int qx=q[mi][a[mi]];
            long long int nx=r[mi];

            long long int b=(qx*10)/(nx*9);
            
            bool g=true;
            
            if(b>0&&(nx*9*b<=qx*10)){
                for(int i=0;i<n;++i){
                    //if(i==mi)
                    //    continue;
                    long long int qy=q[i][a[i]];
                    long long int ny=r[i];
                    if(ny*b*11>=qy*10&&(ny*9*b<=qy*10)){
                    }
                    else{
                        g=false;
                        break;
                    }
                }
            }
            else{
                g=false;
            }
            if(g){
                for(int i=0;i<n;++i){
                    a[i]++;
                }
                counter++;
            }
            else{
                a[mi]++;
            }
            for(int i=0;i<n;++i){
                if(a[i]==p){
                    keep=false;
                }
            }
            
        }

        

        cout<<"Case #"<<T<<": "<<counter;
        cout<<"\n";

        //for(int i=0;i<n;++i){
        //    for(int j=0;j<p;++j){
        //        cout<<q[i][j]<<" ";
        //    }
        //    cout<<endl;
        //}

        
    }
    return 0;
}
