#include <iostream>
#include <fstream>
#include <tgmath.h>

using namespace std;

int main()
{
    ifstream my_input;
    my_input.open("C-small-1-attempt1.in");
    ofstream my_output;
    my_output.open("output.txt");
    unsigned int T;
    my_input >> T;

    for(unsigned int m =0;m<T;m++) {
        unsigned int N, K;
        my_input >> N >> K;
        bool* stalls = new bool [N];
        bool* is_max_of_min = new bool [N];
        bool* is_max_of_max = new bool [N];
        int* Left = new int [N];
        int* Right = new int [N];
        int* Min = new int [N];
        int* Max = new int [N];
        unsigned int max_of_min=0;
        unsigned int max_of_max=0;
        unsigned int choosen;
        for(unsigned int i=0;i<N;i++) {
            stalls[i] = 0;
            Right[i] = 0;
        }
        for(unsigned int j=0;j<K;j++) {
            int last_taken=-1;
            max_of_min = 0;
            max_of_max = 0;
            choosen = -1;
            for(unsigned int i=0;i<N;i++) {
                is_max_of_min[i]=0;
                is_max_of_max[i]=0;
                Right[i]=0;
                Left[i]=0;
                Min[i]=0;
                Max[i]=0;

            }
            for(unsigned int i=0;i<N;i++) {
                if(stalls[i]==1) {
                    Left[i] = -1;
                    Right[i] = -1;
                    last_taken = i;
                } else {
                    Left[i] = i-1-last_taken;
                    for(unsigned int k=last_taken+1;k<i;k++) {
                        Right[k]++;
                    }
                }
            }
            for(unsigned int i=0;i<N;i++){
                if(Right[i]<Left[i]) {
                    Min[i]=Right[i];
                    Max[i]=Left[i];
                } else {
                    Min[i]=Left[i];
                    Max[i]=Right[i];
                }
            }
            for(unsigned int i=0;i<N;i++) {
                if(Min[i]>(int)max_of_min) {
                    max_of_min = Min[i];
                }
            }
            for(unsigned int i=0;i<N;i++) {
                if(Min[i]==(int)max_of_min) {
                    is_max_of_min[i] =1;
                }
            }
            for(unsigned int i=0;i<N;i++) {
                if(is_max_of_min[i]==1 && Max[i]>(int)max_of_max) {
                    max_of_max = Max[i];
                }
            }
            for(unsigned int i=0;i<N;i++) {
                if(is_max_of_min[i]==1 && Max[i]==(int)max_of_max) {
                    is_max_of_max[i] =1;
                }
            }
            bool done =0;
            for(unsigned int i=0;i<N && !done;i++){
                if(is_max_of_max[i]) {
                    stalls[i]=1;
                    done=1;
                    choosen = i;
                }
            }

        }
    my_output << "Case #" << m+1 << ": " << Max[choosen] << " " << Min[choosen] << endl;
    delete [] stalls;
    delete [] is_max_of_max;
    delete [] is_max_of_min;
    delete [] Left;
    delete [] Right;
    delete [] Min;
    delete [] Max;
    }
    my_input.close();
    my_output.close();
    return 0;
}
