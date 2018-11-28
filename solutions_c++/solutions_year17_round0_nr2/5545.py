#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream getInput("C:\\Users\\Eugene\\Documents\\GCJp2.txt");
    ofstream ProblemOutput;
    ProblemOutput.open ("C:\\Users\\Eugene\\Documents\\GCJp2Output.txt");

    int T;
    getInput >> T;

    for(int x = 1; x <= T; x++){

        string number;
        getInput >> number;
        int N[number.length()];

        for(int y = 0; y < number.length(); y++){
            N[y] = number[y] - 48;
        }

        bool done = false;

        while(!done){ //handle pesky 0 case
            done = true;
            for(int z = 1; z < number.length(); z++){
                if(N[z] >= N[z-1])
                    continue;

                N[z-1]--;
                for(int a = z; a < number.length(); a++)
                    N[a] = 9;
                done = false;
                break;
            }
        }

        ProblemOutput << "Case #" << x << ": ";

        int itterate = 0;

        if(N[0] == 0)
            itterate = 1;

        for(itterate; itterate < number.length(); itterate++){
            ProblemOutput << N[itterate];
        }

        if(x != T)
        {
            ProblemOutput << "\n";
        }
    }

    ProblemOutput.close();
    return 0;
}