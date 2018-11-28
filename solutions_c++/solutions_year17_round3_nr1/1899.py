#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <math.h>
#include <iomanip>

//const double PI = 3.1415926535897932384626433832795028841971;
const double PI = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211707;
//3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249
using namespace std;

bool bigger(pair<long long, long long>a, pair<long long, long long>b) {
    return(a.first < b.first);
}

string solve(int N, int K) {
    //cout << "N:" << N << "K:" << K << endl;
    long double areaF = 0.0;
    long long area = 0;
    double maxP = 0.0;
    pair<long long, long long> biggest;
//map<int, vector<int>> RTOH;
    //map<int, vector<int>> HTOR;
    //vector<int> rs;
    //vector<int> hs;
    map<double, vector<pair<long long, long long> > > x;
    vector<pair<long long, long long> > pans;
    for (int i = 0; i < N; ++i) {
        long long radius, height;
        cin >> radius >> height;
        //rs.push_back(radius);
        //RTOH[radius].push_back(height);
        //RTOH[height].push_back(radius);
        //hs.push_back(height);
        //x[2*radius*height].push_back(make_pair(radius, height));
        pans.push_back(make_pair(2*radius*height, radius));
        long long full = pow(radius,2) + (2*radius*height);
        //cout << radius << "R" << height << endl;
        //cout << full << endl;;
        if (maxP < full) { maxP = full; biggest = make_pair(2*radius*height, radius);  }
    }

/*for (int i = 0; i < pans.size(); ++i) {
        cout << pans[i].first << "n" << pans[i].second << " ";
    }
    cout << endl;*/

    sort(pans.begin(), pans.end(), bigger);
    vector<pair<long long, long long> >::iterator it = find(pans.begin(), pans.end(), biggest);
    long long maxR = (*it).second;
    area += biggest.first;
    pans.erase(it);
    
    //cout << "SI" << x.size();
    //cout << x[biggest][0].first << " " << x[biggest][0].second << endl;

    /*for (int i = 0; i < pans.size(); ++i) {
        cout << pans[i].first << "m" << pans[i].second << " ";
    }
    cout << endl;*/

    int count = 0;
    for(int i = pans.size()-1; i >= 0; --i, ++count) {
        if (count == K-1) break;
        //pair<int, int> rh = x[pans[i]][0];
        //cout << pans[i].first << " " << pans[i].second << endl;
        area += pans[i].first;
        maxR = max(maxR, pans[i].second);
       // x[pans[i]].erase(x[pans[i]].begin());
    }
    //cout << "MaxR:" << maxR << endl;
    area += pow(maxR, 2);
    //cout <<  endl ;
    areaF = area * PI;
    stringstream ss;
    ss.setf(ios::fixed);
    ss << setprecision(9) << areaF;
    return ss.str();
}

int main() {

    ofstream fout;
    fout.open("output.txt");

    if (fout.is_open()) {
        int N, K;

        int num_tests = 0;
        cin >> num_tests;

        unsigned count = 1;
        while ( count <= num_tests ) {
            cin >> N >> K;
            fout.precision(7);
            fout << "Case #" << count << ": ";
            fout << solve(N, K) << endl; 
            count++;
        }
        fout.close();
    } else {
        cout << "Can't open file!";
    }
    return 0;
}