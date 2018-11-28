#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream getInput("C:\\Users\\Eugene\\Documents\\GCJp3.txt");
    ofstream ProblemOutput;
    ProblemOutput.open ("C:\\Users\\Eugene\\Documents\\GCJp3Output.txt");

    int val;
    int T;

    getInput >> T;

    for(int x = 1; x <= T; x++){
        int N;
        int K;

        getInput >> N;
        getInput >> K;

        int arr[N+2];

        for(int a = 1; a <= N; a++)
            arr[a] = 0;

        arr[0] = 1;
        arr[N+1] = 1;
        int beg = 0;

        for(int p = 0; p < K; p++){
            int bestBegin = 0;
            int bestEnd = 0;
            for(int a = 0; a < N+2; a++){
                if(arr[a] == 1){
                    if(a-beg > bestEnd-bestBegin){
                        bestBegin = beg;
                        bestEnd = a;
                    }
                    beg = a;
                }
            }
            if(p == K-1){
                arr[((bestEnd-bestBegin)/2)+bestBegin]++;
                val = ((bestEnd-bestBegin)/2)+bestBegin;
            }
            else
                arr[((bestEnd-bestBegin)/2)+bestBegin]++;
        }


        int rightBound = 0;
        int leftBound = 0;

        for(int s = val+1; s < N+2; s++){
            if(arr[s]==0)
                rightBound++;
            else
                break;
        }

        for(int s = val-1; s >= 0; s--){
            if(arr[s]==0)
                leftBound++;
            else
                break;
        }

        ProblemOutput << "Case #" << x << ": " << rightBound << " " << leftBound;
        if(x!=T)
            ProblemOutput << "\n";

    }



    ProblemOutput.close();
    return 0;
}
