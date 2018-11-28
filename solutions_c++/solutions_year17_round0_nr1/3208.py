// Acroph created at 2017-04-08 14:07:28
// ptx9363@gmail.com for more cantact




#include <iostream>
#include <string>

using namespace std;

int main(){
    int T;
    string line;

    cin >> line;
    T = stoi(line);

    string pancake;
    int K;
    for (int t=0; t<T;t++){
        cin >> pancake;
        cin >> K;
        
        int n = pancake.length();
        
        int head = 0;
        int counter = 0;
        while (head < n-K+1){
            if (pancake[head] == '+'){
                head++;
            }
            else {
                counter++;
                for(int i = head; i < head+K; i++)
                    if (pancake[i] == '+')
                        pancake[i] = '-';
                    else
                        pancake[i] = '+';
                head++;
            }
        }
        
        bool success = true;
        for(int i=0; i<n; i++)
            success = success && (pancake[i] == '+');

        if (success)
            cout << "Case #" << t+1 << ": " << counter << endl;
        else
            cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
    }

    
    return 0;
}
