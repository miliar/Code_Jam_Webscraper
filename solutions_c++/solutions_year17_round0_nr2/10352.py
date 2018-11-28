#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

typedef vector<int> vi;

vi make_number_vector_S(int N);
vi make_number_vector_L(int N);


int main()
{
    //get T go through Tlines
    //get N
    //define a tidy number as number_array == sorted(number_array)
    //start from N and decrease to 1
    int T,N;
    vi a;
    vi as;
    ofstream fout("B-small-attempt2.out");
    ifstream fin("B-small-attempt2.in");
    fin >> T;
    for(int i  = 0;i<T;i++){
        fin >> N;
        for(int j = N;j>0;j--){
            a = make_number_vector_S(j);
            as = a;
            sort(as.begin(),as.end());
            if(a == as){
                    cout<<"Case #" << i+1 << ": "<< j << endl;
                fout << "Case #" << i+1 << ": "<< j << endl;
                break;
            }
        }
    }
}

vi make_number_vector_S(int N){
    vi num;
    num.push_back(N/1000);
    num.push_back((N/100) - ((N/1000) * 10));
    num.push_back((N/10) - ((N/100) * 10));
    num.push_back(N - ((N/10)*10));
    return num;
}
