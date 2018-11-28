#include <iostream>
using namespace std;
int main(int argc, char const *argv[]) {
    int num;
    cin >> num;
    for(int numruns = 0;numruns<num;numruns++) {
        string temp;
        cin >> temp;
        while(true) {
            bool done = true;
            for (int x = 0; x<temp.length()-1;x++) {
                if (temp[x]>temp[x+1]) {
                    temp = temp.substr(0,x) + string(1, (temp[x]-1)) + string(temp.length()-x-1, '9');
                    done = false;
                    break;
                }
            }
            if (done) {
                break;
            }
        }
        temp.erase(0, min(temp.find_first_not_of('0'), temp.size()-1));
        cout << "Case #" << numruns+1<< ": " << temp << endl;
    }
    return 0;
}