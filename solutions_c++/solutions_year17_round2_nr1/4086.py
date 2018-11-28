#include<bits/stdc++.h>
using namespace std;

bool myfunction(pair<int,int>p1,pair<int,int>p2){
    return p1.first<p2.first;
}
int main(){

    ifstream myReadFile;
    myReadFile.open("input.in");
    ofstream myfile;
    myfile.open ("output.out");
    int t;
    myReadFile>>t;
    int c=1;

    while(t--){


        int D,N;
        myReadFile>>D>>N;
        vector<pair<int,int> > horses(N);
        for(int i=0;i<N;i++){
            myReadFile>>horses[i].first>>horses[i].second;
        }
        sort(horses.begin(),horses.end(),myfunction);

        vector<double>catchs(N-1);
        for(int i=0;i<N-1;i++){
                if(horses[i].second<=horses[i+1].second){catchs[i]=-1;continue;}
                catchs[i]=(double)(horses[i+1].first*horses[i].second-horses[i].first*horses[i+1].second)/(horses[i].second-horses[i+1].second);
                if(catchs[i]>=D)catchs[i]=-1;
        }
        double ret=(double)horses[0].second*D/(D-horses[0].first);
        double x;

        for(int i=0;i<N-1;i++){
            if(catchs[i]==-1)break;
            else {
                ret=min(ret,(double)horses[i+1].second*D/(D-horses[i+1].first));
            }
        }
        myfile<<"Case #"<<c<<": ";
        myfile<<setprecision(10)<<ret;
        myfile<<endl;
        c++;
    }
    return 0;
}
