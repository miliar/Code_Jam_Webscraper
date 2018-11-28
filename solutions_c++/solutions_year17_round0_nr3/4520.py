#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct tupla{
    long L;
    long R;
    tupla(long l,long r){
        L=l;
        R=r;
    }
};


void print_vt(vector<tupla> VT){
    for(auto v:VT){
        cout<<"("<<v.L<<","<<v.R<<")"<<endl;
    }

}

int main()
{
    long test,caso=1,N,k,i;
    long aux_L,aux_R;
    cin>>test;
    vector<tupla> VT;
    while(caso<=test){
    cin>>N;
    cin>>k;
    k--;
    if(N%2==1)
        VT.push_back(tupla(N/2,N/2));
    else
        VT.push_back(tupla(N/2-1,N/2));
    i=0;
    while(VT.size()<N){
        if(VT[i].L%2==0&&VT[i].R%2==0){
            VT.push_back(tupla((VT[i].L-1)/2,VT[i].R/2));
            VT.push_back(tupla((VT[i].L-1)/2,VT[i].R/2));
        }
        else{
            VT.push_back(tupla((VT[i].L)/2,VT[i].R/2));
            VT.push_back(tupla((VT[i].L-1)/2,(VT[i].R-1)/2));
            }

        i++;
    }
    sort(VT.begin(),VT.end(),[](tupla a,tupla b){
        if(min(a.R,a.L)!=min(b.R,b.L))
            return min(a.R,a.L)>min(b.R,b.L);
        else
            return max(a.R,a.L)>max(b.R,b.L);

    });
    cout<<"Case #"<<caso<<": "<<max(VT[k].L,VT[k].R)<<" "<<min(VT[k].L,VT[k].R)<<endl;
    caso++;
    VT.clear();
    }
    return 0;
}
