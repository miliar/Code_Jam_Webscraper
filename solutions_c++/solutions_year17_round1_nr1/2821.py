#include <bits/stdc++.h>
using namespace std;

char arr[30][30];

int main()
{
    int tetC;
    cin >> tetC;
    for(int cnt = 0; cnt < tetC; cnt++){
        int rw , cl;
        cin >> rw >> cl;
        map<char, vector<pair<int,int> > > prVec;
        for(int rcn = 0; rcn < rw; rcn++) {
            for(int ccn = 0; ccn < cl; ccn++) {
                cin >> arr[rcn][ccn];
                if(arr[rcn][ccn] != '?') {
                    if(prVec.find(arr[rcn][ccn]) == prVec.end()) {
                        vector<pair<int,int> > tmpVec;
                        prVec[arr[rcn][ccn]] = tmpVec;
                    }
                    prVec[arr[rcn][ccn]].push_back(make_pair(rcn,ccn));
                }
            }
        }
        map<char , pair<int,int> > dmMap;
        map<char, vector<pair<int,int> > >::iterator trv;
        for(trv = prVec.begin(); trv != prVec.end(); trv++) {
            char curChar = trv->first;
            vector<pair<int,int> > curVec = trv->second;
            //sort(curVec.begin() , curVec.end());
            int xmn,ymn, xmx,ymx;
            xmn = curVec[0].first;
            ymn = curVec[0].second;

            xmx = curVec[curVec.size() -1].first;
            ymx = curVec[curVec.size() -1].second;

            for(int curx = xmn; curx <= xmx; curx++) {
                for(int cury = ymn; cury <= ymx; cury++) {
                    arr[curx][cury] = curChar;
                }
            }
            dmMap[curChar] = make_pair(xmx - xmn + 1, ymx - ymn + 1);
        }
        ////////////// hor cut pass
        for(trv = prVec.begin(); trv != prVec.end(); trv++) {
            char curChar = trv->first;
            vector<pair<int,int> > curVec = trv->second;
            sort(curVec.begin(), curVec.end());
            int lastRowY = curVec[curVec.size() -1].second;
            int curMNx = curVec[0].first;
            int curMXx = curVec[curVec.size() -1].first;
            for(int curY = lastRowY + 1; curY < cl; curY++) {
                bool al = true;
                for(int curX = curMNx; curX <= curMXx; curX++) {
                    if(arr[curX][curY] != '?'&& arr[curX][curY] != curChar) {
                        al = false;
                        break;
                    }
                }
                if(al) {
                    for(int curX = curMNx; curX <= curMXx; curX++) {
                        arr[curX][curY] = curChar;
                        prVec[curChar].push_back(make_pair(curX,curY));
                    }
                }
                else {
                    break;
                }
            }

            ////////////////////////////

            int fRowY = curVec[0].second;
            for(int curY = fRowY - 1; curY >= 0; curY--) {
                bool al = true;
                for(int curX = curMNx; curX <= curMXx; curX++) {
                    if(arr[curX][curY] != '?'&& arr[curX][curY] != curChar) {
                        al = false;
                        break;
                    }
                }
                if(al) {
                    for(int curX = curMNx; curX <= curMXx; curX++) {
                        arr[curX][curY] = curChar;
                        prVec[curChar].push_back(make_pair(curX,curY));
                    }
                }
                else {
                    break;
                }
            }

        }

        ///////////////////////////////////
        for(trv = prVec.begin(); trv != prVec.end(); trv++) {
            char curChar = trv->first;
            vector<pair<int,int> > curVec = trv->second;
            sort(curVec.begin(), curVec.end());
            int lastRowX = curVec[curVec.size() -1].first;
            int curMNy = curVec[0].second;
            int curMXy = curVec[curVec.size() -1].second;
            for(int curX = lastRowX + 1; curX < rw; curX++) {
                bool al = true;
                for(int curY = curMNy; curY <= curMXy; curY++) {
                    if(arr[curX][curY] != '?' && arr[curX][curY] != curChar) {
                        al = false;
                        break;
                    }
                }
                if(al) {
                    for(int curY = curMNy; curY <= curMXy; curY++) {
                        arr[curX][curY] = curChar;
                        prVec[curChar].push_back(make_pair(curX,curY));
                    }
                }
                else {
                    break;
                }
            }
            //////////////////////

            int fCol = curVec[0].first;
            for(int curX = fCol - 1; curX >= 0; curX--) {
                bool al = true;
                for(int curY = curMNy; curY <= curMXy; curY++) {
                    if(arr[curX][curY] != '?' && arr[curX][curY] != curChar) {
                        al = false;
                        break;
                    }
                }
                if(al) {
                    for(int curY = curMNy; curY <= curMXy; curY++) {
                        arr[curX][curY] = curChar;
                        prVec[curChar].push_back(make_pair(curX,curY));
                    }
                }
                else {
                    break;
                }
            }

        }

        cout << "Case #"<<cnt+1<<":"<<endl;
        for(int rcn = 0; rcn < rw; rcn++) {
            for(int ccn = 0; ccn < cl; ccn++) {
                cout << arr[rcn][ccn];
            }
            cout << endl;

        }
    }
    return 0;
}
