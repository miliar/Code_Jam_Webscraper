#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream getPancakes("C:\\Users\\Eugene\\Documents\\GCJp1.txt");
    ofstream ProblemOutput;
    ProblemOutput.open ("C:\\Users\\Eugene\\Documents\\GCJp1Output.txt");

    int T;
    getPancakes >> T;

    string pancakes;
    int K;
    for(int x = 1; x <= T; x++){
        bool flipArr[1000];

        char pancake;
        int counter = 0;

        do{
            getPancakes >> pancake;
            pancake == '+' ? flipArr[counter] = 1 : flipArr[counter] = 0;
            counter++;

        }while(getPancakes.peek() == '+' || getPancakes.peek() == '-');

        bool flipArrBounded[counter];

        for(int y = 0; y < counter; y++)
            flipArrBounded[y] = flipArr[y];


        int steps = 0;
        getPancakes >> K;

        for(int y = counter-1; y >= K-1; y--){
            if(flipArrBounded[y])
                continue;

            for(int z = y; z > y-K; z--)
                flipArrBounded[z] = !flipArrBounded[z];
            steps++;
        }

        bool solvable = true;

        for(bool a : flipArrBounded){
            if(!a){
                solvable = false;
                break;
            }
        }

        ProblemOutput << "Case #" << x << ": ";

        solvable ? ProblemOutput << steps : ProblemOutput << "IMPOSSIBLE";

        if(x != T)
            ProblemOutput << "\n";
    }
    ProblemOutput.close();
    return 0;
}


