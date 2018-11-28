#include <iostream>
#include <map>

using namespace std;

int main()
{
    int t, r, c;
    char grids[30][30];
    cin >> t;
    for(int icase = 1; icase <= t; icase++)
    {
        map<char,int> max_c;
        map<char,int> max_r;
        map<char,int> min_c;
        map<char,int> min_r;
        char list[26];
        int num_char = 0;

        cin >> r >> c;
        for(int irow = 0; irow < r; irow++)
        {
            cin >> grids[irow];
            grids[irow][c] = '\0';
        }

        cout << "Case #" << icase << ":" << endl;

        for(int irow = 0; irow < r; irow++)
        {
            for(int icol = 0; icol < c; icol++)
            {
                if(grids[irow][icol] != '?')
                {
                    int r_min = irow;
                    while(r_min > 0 && grids[r_min-1][icol] == '?')
                    {
                        grids[r_min-1][icol] = grids[irow][icol];
                        r_min--;
                    }

                    list[num_char] = grids[irow][icol];
                    max_c[list[num_char]] = icol;
                    max_r[list[num_char]] = irow;
                    min_c[list[num_char]] = icol;
                    min_r[list[num_char]] = r_min;
                    num_char++;
                    //debug
                    //cout << grids[irow][icol] << ": " << r_min << ", " << icol << endl;
                }
            }
        }
        // leftward expansion
        for(int ichar = 0; ichar < num_char; ichar++)
        {
            char ch = list[ichar];
            int icol;
            for(icol = max_c[ch]; icol > 0; icol--)
            {
                int irow = max_r[ch] + 1;
                while(irow > min_r[ch] && grids[irow-1][icol-1] == '?'){irow--;}
                if(irow > min_r[ch])
                    break;
                for(irow = max_r[ch]; irow >= min_r[ch]; irow--)
                {
                    grids[irow][icol-1] = ch;
                }
            }
            min_c[ch] = icol;
        }
        // downward expansion
        for(int ichar = 0; ichar < num_char; ichar++)
        {
            char ch = list[ichar];
            int irow;
            for(irow = max_r[ch]; irow + 1 < r; irow++)
            {
                int icol = max_c[ch] + 1;
                while(icol > min_c[ch] && grids[irow+1][icol-1] == '?'){icol--;}
                if(icol > min_c[ch])
                    break;
                for(icol = max_c[ch]; icol >= min_c[ch]; icol--)
                {
                    grids[irow+1][icol] = ch;
                }
            }
            max_r[ch] = irow;
        }
        // rightward expansion
        for(int ichar = 0; ichar < num_char; ichar++)
        {
            char ch = list[ichar];
            int icol;
            for(icol = max_c[ch]; icol + 1 < c; icol++)
            {
                int irow = max_r[ch] + 1;
                while(irow > min_r[ch] && grids[irow-1][icol+1] == '?'){irow--;}
                if(irow > min_r[ch])
                    break;
                for(irow = max_r[ch]; irow >= min_r[ch]; irow--)
                {
                    grids[irow][icol+1] = ch;
                }
            }
        }

        for(int irow = 0; irow < r; irow++)
        {
            cout << grids[irow] << endl;
        }

    }

    return 0;
}

