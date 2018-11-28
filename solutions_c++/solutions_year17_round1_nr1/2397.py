#include <iostream>
#include <vector>
using namespace std;

int main() {
    int numberTestCases;
    cin >> numberTestCases;
    for (int i = 0; i < numberTestCases; i++)
    {
        // INPUT
        int rows, cols;
        cin >> rows >> cols;
        // rows = 4;
        // cols = 3;
        vector<vector<int> > cake (rows, vector<int>(cols, -9));
        // int rsize = (int) cake.size();
        // int csize = (int) cake[1].size();
        for (int j = 0; j < rows; j++)
        {
            for (int k = 0; k < cols; k++)
            {
                //// // cerr << "here" << endl;
                char a;
                cin >> a;
                cake[j][k] = a;
            }
        }

        // PROCESSING
        //// cerr << "error a";
        for (int l = 0; l < rows; l ++)
        {
            for (int m = 0; m < cols; m ++)
            {
                //// cerr << "error b";
                if (cake[l][m] == '?')
                {
                    int rownumber = l;
                    while ((cake [rownumber][m] == '?') and (rownumber < (rows-1)))
                    {
                        //// cerr << "error c";
                        rownumber = rownumber + 1;
                    }
                    //// cerr << "error d";
                    cake[l][m] = cake[rownumber][m];
                    /*Nothing below*/
                    if (cake[l][m] == '?')
                    {
                        int rownumB= l;
                        //// cerr << "error e";
                        while ((cake [rownumB][m] == '?') and (rownumB > 0))
                        {
                            //// cerr << "error f";
                            rownumB = rownumB -1;
                        }
                        //// cerr << "error g";
                        cake[l][m] = cake[rownumB][m];
                    }
                }
            }
        }

        /*ALL THAT REMAINS IS A COLUMN OF QUESTION MARKS*/
        for (int abcols = 0; abcols < cols; abcols ++)
        {
            if (cake[0][abcols] == '?')
            {
                // int nextnonqcol = abcols;
                // // Going Right
                // while (cake[0][nextnonqcol] == '?') && (a

                // Going Left if needed

                // Setting value

                //cerr << "here" << endl;
                int nextnonqcol = abcols;
                while ((cake[0][nextnonqcol] == '?') &&(nextnonqcol < (cols-1)))
                {
                    nextnonqcol ++;
                }
                //cerr << "a:" << nextnonqcol;
                if (cake[0][nextnonqcol] == '?')
                {
                    nextnonqcol = abcols;
                    while ((cake[0][nextnonqcol] == '?') && (nextnonqcol > 0))
                    {
                        nextnonqcol --;
                    }
                }
                //cerr << "b:" << nextnonqcol;
                for (int rowg = 0; rowg < rows; rowg++)
                {
                    cake[rowg][abcols] = cake[rowg][nextnonqcol];
                }               
            }
        }
        // PRINTING
        cout << "Case #" << i+1 << ":\n";
        for (int y = 0; y < rows; y++)
        {
            //// cerr << "error h";
            for (int z = 0; z < cols; z ++)
            {
                //// cerr << "error i";
                cout << (char)cake[y][z];
                //// cerr << "error j";
            }
            cout << endl;
        }
        //// cerr << "error k";
    }
    return 0;
}