#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {

    uint64_t t, n;
    string s;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

    for (int i = 1; i <= t; ++i) {
        cin >> n;  // read n.

        uint64_t j = 0;
        for (j = n; j > 0; --j) {

            uint64_t k = j;

            vector<uint64_t> number;
            do {
                number.push_back(k%10);
                k /= 10;
            }while (k != 0);

            int counter = 0;
            for(int l = 0; l < number.size() - 1 ; ++l)
            {
                if( (l+1 >= 0) && (number[l] >= number[l+1]) )
                {
                    ++counter;
                } else {
                    break;
                }
            }

            if(counter == number.size() - 1) {
                cout << "Case #" << i << ": " << j << endl;
                break;
            }
        }
   }
}

