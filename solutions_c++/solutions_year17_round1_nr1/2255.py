#include <iostream>

using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int a0=1; a0<=T; a0++)
    {
        int r, c;
        cin >> r >> c;
        string mat[r];
        string s = "?";
        for(int i=0; i<c-1; i++)
            s += '?';
        string fline;
        bool fbline = false;
        int rank=0;

        for(int i=0; i<r; i++)
        {
            cin >> mat[i];
            if(mat[i] != s)
            {
                int j=0;
                char first, c;
                while(mat[i][j] == '?')
                    j++;
                first = mat[i][j];
                c = first;
                for(int k=j+1; k<c; k++)
                {
                    if(mat[i][k] == '?')
                        mat[i][k] = c;
                    else
                        c = mat[i][k];
                }

                for(int k=0; k<j; k++)
                    mat[i][k] = first;
                if(!fbline)
                {
                    fline = mat[i];
                    fbline = true;
                    rank = i;
                }
            }
        }

        for(int i=0; i<rank; i++)
            mat[i] = fline;

        for(int i=rank+1; i<r; i++)
        {
            if(mat[i] != s)
                fline = mat[i];
            else
                mat[i] = fline;
        }

        cout << "Case #" << a0 << ":" << endl;
        for(int i=0; i<r; i++)
            cout << mat[i] << endl;

    }

    return 0;
}
