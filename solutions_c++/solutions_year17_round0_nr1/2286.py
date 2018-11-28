#include<iostream>
#include<string>

using namespace std;

int main() {
    int ins, cas, flip;
    string cakes;
    bool succ=true;

    cin >> ins;

    for (int i=0;i<ins;i++) {
        cin >> cakes;

        cin >> flip;

        int flips=0;
        succ=true;

        for (int b=0; b<cakes.length(); b++) {
            if (cakes[b]=='-') {
                flips++;
            
                if ((b+flip)>cakes.length()) {
                    if (succ) cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << "\n";
                    succ = false;
                } else for (int c=0; c<flip; c++) {
                    if      (cakes[b+c]=='-') cakes[b+c]='+';
                    else if (cakes[b+c]=='+') cakes[b+c]='-';
                }            
            }                
        }

        if (succ) cout << "Case #" << i+1 << ": " << flips << "\n";
    }	
}
