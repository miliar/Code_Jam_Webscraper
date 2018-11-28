#include <fstream>
#include <iomanip>

using namespace std;

int main() {
    ifstream infile("A-large.in");
    ofstream outfile("A-large.out");


    int T;
    infile>>T;
    for(int t=1;t<=T;++t){
        int d, n;
        infile>>d>>n;
        double time = 0;
        for(int i=0;i<n;++i){
            int k, s;
            infile>>k>>s;
            time = max(time, static_cast<double>(d-k) / s);
        }
        outfile<<"Case #"<<t<<": "<<setprecision(16)<<(d/time)<<endl;
    }

    infile.close();
    outfile.close();
    return 0;
}