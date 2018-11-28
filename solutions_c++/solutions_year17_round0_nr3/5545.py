#include <fstream>
#include <string>
#include <iostream>
#include <vector>
using namespace std;




int main(int argc, char **argv) {

    ifstream input("C-small-1-attempt1.in");
    ofstream output("output.out");
    int T,test;
    long long int N,K,maxspace,mid,index;
    vector<long long int> spaces;
    input >> T;

    for(int t=0; t<T; t++) {
        spaces.clear();
        K=0;
        N=0;
        input >> N;
        input >> K;


        if(K==N) {
             output << "Case #" << t+1 << ": 0 0" << endl;
            continue;
        }
        if(N%2==0) {
            mid=N/2;

        } else mid=N/2+1;
        spaces.push_back(mid-1);
        spaces.push_back(N-mid);
        maxspace=N;
        K--;
        /*for(int i=0; i<spaces.size(); i++) {
            cout << "Vector position " << i <<" = " << spaces.at(i)<<endl;
        }*/


        while(K>0) {


            maxspace=spaces.at(0);
            index=0;
            for(long long i=0; i<spaces.size(); i++) {

                if(spaces.at(i)>maxspace) {

                    maxspace=spaces.at(i);
                    index=i;
                }


            }

            if(maxspace%2==0) {
                mid=maxspace/2;
            } else mid=maxspace/2+1;



            spaces.erase(spaces.begin()+index);
            spaces.push_back(mid-1);
            spaces.push_back(maxspace-mid);

            K--;

           /* for(int i=0; i<spaces.size(); i++) {
                cout << "Vector position " << i <<" = " << spaces.at(i)<<endl;
            }
            */




        }



        long long result1 = mid-1;
        long long result2 = maxspace-mid;
         output << "Case #" << t+1 << ": ";
        (result1 > result2)? output<< result1 <<" "<<result2<<endl : output<< result2 <<" "<<result1<<endl;














    }








}


