#include <vector>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <iomanip>

using namespace std;

int main(void) {
    int t, testss =1;
    cin>>t;
    while(testss <= t)
    {
        int N,k ;
        cin>>N>>k;
        double arr[N][2];
        vector<int> sels;
        vector<int> vecss(N);
        
        for(int i=0;i<N;i++)
        {
            cin>>arr[i][0]>>arr[i][1];
        }
        fill(vecss.begin(), vecss.begin() + k, 1);
        double max = -1.0;
        do {
            for (int i = 0; i < N; i++)
            {
                if (vecss[i]) {
                    sels.push_back(i);
                }
            }
            double total = 0.0;
            int lls = sels.size(), mrs_1 = -1;
            for(int i=0;i<lls;i++)
            {
                total += arr[sels[i]][0]* arr[sels[i]][1];
                if( arr[sels[i]][0] > mrs_1)
                    mrs_1 =  arr[sels[i]][0];
            }
            
            total = total*2*3.14159265359;
            total += 3.14159265359*mrs_1*mrs_1;
            
            if(total > max)
                max = total;
            
            sels.clear();
            
        }
        while (prev_permutation(vecss.begin(), vecss.end()));
        cout<<setprecision(10);
        cout<<fixed;
        
        cout<<"Case #"<<testss<<": "<<max<<"\n";
        testss++;
        
    }
    
    return 0;
}
