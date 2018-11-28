#include <iostream>
#include <vector>
using namespace std;

void _main(int t) {
    int d, n;
    cin>>d>>n;
    int *k=new int[n];
    int *s=new int[n];
    vector<double> v;
    for(int i=0;i<n;i++) {
        cin>>k[i]>>s[i];
        v.push_back(double(d - k[i]) / double(s[i]));
    }
    sort(v.begin(), v.end());
    double res = double(d) / v[n-1];
    cout.precision(6);
    cout<<fixed;
    cout<<"Case #"<<t<<": "<<res<<endl;
}

int main(int argc, char* argv[])
{
    int t;
    cin>>t;
    for(int i = 0; i < t; i++) {
        _main(i+1);
    }

    return 0;
}
