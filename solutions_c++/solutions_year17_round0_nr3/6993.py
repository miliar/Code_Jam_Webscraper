#include <fstream>
#include <vector>


bool filled[1000000];
int left[1000000];
int right[1000000];

void reset(int n) {
    for(int x = 0; x < n; ++x) {
        filled[x] = false;
        left[x] = 0;
        right[x] = 0;
    }
}

int max(int a, int b) {
    return a > b ? a : b;
}

int min(int a, int b) {
    return a < b ? a : b;
}

int main() {

    std::ifstream fin("stalls.in");
    std::ofstream fout("stalls.out");

    int t, n, k;
    fin >> t;

    for(int x = 1; x <= t; ++x) {
        fin >> n >> k;
        reset(n);

        int maxlr, minlr;

        while(true) {
            int l = 0, r = 0;
            for(int y = 0; y < n; ++y) {
                left[y] = l;
                if(filled[y]) l = 0;
                else ++l;
                //fout << left[y] << " ";
            }
            //fout << std::endl;
            for(int y = n-1; y >= 0; --y) {
                right[y] = r;
                if(filled[y]) r = 0;
                else ++r;
            }
            /*
            for(int y = 0; y < n; ++y) {
                //fout << right[y] << " ";
            }
            //fout << std::endl << std::endl;*/

            std::vector<int> bestmin;
            int bestmax = 0;
            minlr = 0;
            maxlr = 0;
            for(int y = 0; y < n; ++y) {
                if(filled[y]) continue;

                if(minlr < min(left[y], right[y])) {
                    bestmin.clear();
                    bestmin.push_back(y);
                    minlr = min(left[y], right[y]); 

                    bestmax = y;
                    maxlr = max(left[y], right[y]);               
                }else if(minlr == min(left[y], right[y])) {
                    bestmin.push_back(y);       
                    if(maxlr < max(left[y], right[y])) {
                        maxlr = max(left[y], right[y]);
                        bestmax = y;
                    }       
                }
            }

            if(bestmin.size() == 1) {
                filled[bestmin[0]] = true;
            }else {
                filled[bestmax] = true;
            }

            /*
            for(int y = 0; y < n; ++y) {
                fout << filled[y] << " ";
            }
            fout << std::endl;*/

            --k;
            if(k == 0) break;
        }



        /*
        int l = 0, r = 0;
        for(int y = 0; y < n; ++y) {
            left[y] = l;
            if(filled[y]) l = 0;
            else ++l;
            fout << left[y] << " ";
        }
        fout << std::endl;
        for(int y = n-1; y >= 0; --y) {
            right[y] = r;
            if(filled[y]) r = 0;
            else ++r;
        }
        for(int y = 0; y < n; ++y) {
            fout << right[y] << " ";
        }
        fout << std::endl;

        int minlr = 0, maxlr = 0;
        for(int y = 0; y < n; ++y) {
            if(filled[y]) continue;
            if(minlr < min(left[y], right[y])) minlr = min(left[y], right[y]);
            if(maxlr < max(left[y], right[y])) maxlr = max(left[y], right[y]);
            //fout << filled[y] << " ";
        }
        //fout << std::endl;
        */

        fout << "Case #" << x << ": " << maxlr << " " << minlr << std::endl;
    }

    fin.close();
    fout.close();

    return 0;
}



/*


- -



*/
