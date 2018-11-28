
#include <iostream>
#include <stdint.h>
#include <cmath>
#include <string>

using namespace std;

int main()
{
    int T; // number of test cases
    cin >> T;

    long long N[T]; // last number tatiana counted
    for(int i=0;i<T;i++)
    {
        cin >> N[i];
    }
    int nl,nb;
    long long NumberN;
    for(int i=0;i<T;i++)
    {
        NumberN = N[i];
        int firstRun = 0;
        while(true)
        {
            firstRun++;
            long long temp = NumberN;

            int len = 0;
            do {
                ++len; 
                temp /= 10;
                //cout << endl << temp;
            } while (temp);

            temp = NumberN;
            
            int n[len];
            for(int k=0;k<len;k++){
                n[(len-1) - k] = temp % 10;
                temp /=10;  
            }
            bool ok = false;
            int k = 0;
            while(k<len-1)
            {
                if(n[k]<=n[k+1]){
                    // this is ok
                    ok = true;
                }
                else // this is not ok
                {
                    ok = false;
                    k++;
                    k=len - k;
                    break;
                }
                k++;
            }
            
            if(ok == true || len == 1){
                // this is a tidy
                cout << "Case #" << i+1 << ": " << NumberN<< endl;
                firstRun = 0;
                break;
            } else {
                //cout << "dont  ";
                temp = NumberN;
                //cout << temp << endl;
                for(int lst=k;lst<len;lst++){
                    //cout << "===="<<pow(10,lst)*n[len-lst-1]<<endl;
                    long long ingeter = pow(10,lst)*n[len-lst-1];
                    temp = temp - ingeter;
                }
                 //cout << temp << endl;
                NumberN = NumberN - temp - 1;
                //cout << NumberN << endl;
                //string sss = NumberN.to_string();
                //cout << sss;
            }
            
        }
    }
}