#include<cstdio>
#include<vector>
#include<algorithm>
#include <functional>
#define pi 3.1415926535897932384

using namespace std;

FILE *in = fopen("input.txt","r");
FILE *out = fopen("output.txt","w");

int main(){
    int tt;
    fscanf(in,"%d",&tt);
    for(int tc=1;tc<=tt;tc++){
        int n,k;
        fprintf(out,"Case #%d: ",tc);
        fscanf(in,"%d %d" ,&n,&k);
        vector< pair<long long ,long long > > data(n);
        for(int i=0;i<n;i++){
            fscanf(in,"%lld %lld",&data[i].first,&data[i].second);

        }
        vector<double> h;
        double max = 0;
        sort(data.begin(),data.end());
        for(int i=0;i<n;i++){
            double r = data[i].first;
            std::sort(h.begin(),h.end(),std::greater<double>());
            int lim = k-1;
            if(lim>h.size())lim = h.size();
            double hsum=2*r*pi*(double)data[i].second;
            for(int j=0;j<lim;j++){
                hsum+=h[j];
            }
            h.push_back(2*r*pi*(double)data[i].second);
            if(max<pi*r*r + hsum)max = pi*r*r + hsum;
        }
        fprintf(out,"%.9lf\n",max);

    }
    return 0;
}
