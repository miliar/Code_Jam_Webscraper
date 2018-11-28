#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <cmath>
#include <set>
#include <functional>

using namespace std;

int main()
{
    ofstream output("stalls.out");
    int t;
    cin >> t;
    for (int tt=0;tt<t;tt++){
        int n,k;
        cin >> n >> k;

        auto comp = [](const int&  x, const int&  y){ return x > y; };
        multiset< int, std::function<int(const int& x, const int&  y)>> s(comp);

        s.insert(n);
//        cout << "insert: "<<n<<endl;

        for (int j=0;j<k-1;j++){
            int b=*s.begin();
//            cout << "erase: "<<b<<endl;
            s.erase(s.begin());
//            cout << "insert: "<<b/2<<endl;
//            cout << "insert: "<<(b-1-b/2)<<endl;
            s.insert(b/2);
            s.insert(b-1-b/2);
        }





        int ans=max(*s.begin(),0);
//        cout << "top: "<<ans<<endl;
//        cout << "Case #" << tt+1 << ": "<<ans/2<< " "<<max(ans-1-ans/2,0)<< endl;
        output << "Case #" << tt+1 << ": "<<ans/2<< " "<<max(ans-1-ans/2,0)<< endl;
    }


    return 0;
}
