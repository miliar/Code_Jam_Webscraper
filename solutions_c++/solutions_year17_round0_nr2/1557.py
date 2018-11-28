#include <iostream>
#include <string>

using namespace std;
string n;
int length, n_seq[18], tidy_seq[18], is_smaller;

int search_tidy (int string_pos) {
    int i, found=0;
    if (string_pos==0) {
        for (i=n_seq[string_pos]; i>=0; i--) {
            if (i<n_seq[string_pos]) is_smaller=1;
            tidy_seq[string_pos] = i;
            found=search_tidy(string_pos+1);
            if (found) break;
        }
    } else if (string_pos<length-1) {
        if (is_smaller) { //start searching from 9
            tidy_seq[string_pos] = 9;
            found=search_tidy(string_pos+1);
        } else { // start searching from the digit at string_pos
            for (i=n_seq[string_pos]; i>=tidy_seq[string_pos-1]; i--) {
                if (i<n_seq[string_pos]) is_smaller=1;
                tidy_seq[string_pos] = i;
                found=search_tidy(string_pos+1);
                if (found) break;
            }
        }
    } else { //string_pos==length-1 i.e. the final digit
        if (is_smaller) {
            tidy_seq[string_pos] = 9;
            found=1;
        } else if (n_seq[string_pos] >= tidy_seq[string_pos-1] ) {
            tidy_seq[string_pos] = n_seq[string_pos];
            found=1;
        } else found=0; // !is_smaller, i.e. cannot choose 9 && current digit in n is lesser than last digit in tidy_seq
    }
    return found;
}

int main()
{
    int i, j, t;
    cin >> t;
    for (i=1; i<=t; i++) {
        cout << "Case #" << i << ": ";
        cin >> n;
        length = n.length();
        for (j=0; j<length; j++) n_seq[j]=n[j]-'0';
        if (length==1) cout << n;
        else {
            is_smaller=0;
            search_tidy(0);
            for (j=0; j<length; j++) {
                if (tidy_seq[j]>0) cout << char ( tidy_seq[j]+'0' );
            }
        }
        cout << endl;
    }
    return 0;
}
