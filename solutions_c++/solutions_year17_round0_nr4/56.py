//
// Created by XelaPi.
//
#include <iostream>
#include <vector>
#include <map>

using namespace std;

struct Model {
    char style;

    Model() {
        style = '.';
    }

    Model(char firstStyle) {
        style = firstStyle;
    }

    int pointValue() {
        if (style == '.') {
            return 0;
        } else if (style == 'o') {
            return 2;
        } else {
            return 1;
        }
    }
};

bool canBeStar(vector<char *> & rowVector, vector<char *> & columnVector) {
    for (auto & charPointer : rowVector) {
        if (*charPointer == 'x' || *charPointer == 'o') {
            return false;
        }
    }

    for (auto & charPointer : columnVector) {
        if (*charPointer == 'x' || *charPointer == 'o') {
            return false;
        }
    }

    return true;
}

bool canBePlus(vector<char *> & mainDiagVector, vector<char *> & offDiagVector) {
    for (auto & charPointer : mainDiagVector) {
        if (*charPointer == '+' || *charPointer == 'o') {
            return false;
        }
    }

    for (auto & charPointer : offDiagVector) {
        if (*charPointer == '+' || *charPointer == 'o') {
            return false;
        }
    }

    return true;
}

int main() {

    int num;

    cin >> num;

    for (int i = 0; i < num; i++) {
        cout << "Case #" << (i + 1) << ": ";

        int size, initModels;

        cin >> size;
        cin >> initModels;

        Model * runway = new Model[size * size];

        for (int j = 0; j < initModels; ++j) {
            char style;
            int x, y;

            cin >> style;

            cin >> y;
            cin >> x;

            x--;
            y--;

            runway[y * size + x].style = style;
        }

        vector<vector<char *>> rowVectors;
        vector<vector<char *>> columnVectors;

        for (int k = 0; k < size; ++k) {
            vector<char *> newRowVector;
            vector<char *> newColumnVector;

            for (int j = 0; j < size; ++j) {
                newRowVector.push_back(&runway[k * size + j].style);
                newColumnVector.push_back(&runway[j * size + k].style);
            }

            rowVectors.push_back(newRowVector);
            columnVectors.push_back(newColumnVector);
        }

        vector<vector<char *>> mainDiagVectors;
        vector<vector<char *>> offDiagVectors;

        for (int l = size - 1; l >= 0; --l) {
            vector<char *> mainDiagVector;
            vector<char *> offDiagVector;

            for (int j = 0; j < size - l; ++j) {
                mainDiagVector.push_back(&runway[j * size + j + l].style);
                offDiagVector.push_back(&runway[(size - 1 - j) * size + j + l].style);
            }

            mainDiagVectors.push_back(mainDiagVector);
            offDiagVectors.push_back(offDiagVector);
        }

        for (int l = 1; l < size; ++l) {
            vector<char *> mainDiagVector;
            vector<char *> offDiagVector;

            for (int j = 0; j < size - l; ++j) {
                mainDiagVector.push_back(&runway[(j + l) * size + j].style);
                offDiagVector.push_back(&runway[(size - 1 - j - l) * size + j].style);
            }

            mainDiagVectors.push_back(mainDiagVector);
            offDiagVectors.push_back(offDiagVector);
        }

        map<pair<int, int>, string> additions;

        unsigned long long score = 0;

        for (int m = 0; m < (size + 1) / 2; ++m) {
            for (int j = m; j < size - m; ++j) {
                int y = m;
                int x = j;

                Model & current = runway[y * size + x];

                bool plus = current.style == '+' || canBePlus(mainDiagVectors[size - 1 - x + y],
                                                              offDiagVectors[(size - 1) * 2 - x - y]);

                bool star = current.style == 'x' || canBeStar(rowVectors[y], columnVectors[x]);

                if (current.style == '.') {
                    if (plus) {
                        current.style = '+';
                        additions[make_pair(x, y)] = "+ " + to_string(y + 1) + " " + to_string(x + 1);
                    } else if (star) {
                        current.style = 'x';
                        additions[make_pair(x, y)] = "x " + to_string(y + 1) + " " + to_string(x + 1);
                    }
                }
            }

            for (int j = m; j < size - m; ++j) {
                int y = j;
                int x = size - 1 - m;

                Model & current = runway[y * size + x];

                bool plus = current.style == '+' || canBePlus(mainDiagVectors[size - 1 - x + y],
                                                              offDiagVectors[(size - 1) * 2 - x - y]);

                bool star = current.style == 'x' || canBeStar(rowVectors[y], columnVectors[x]);

                if (current.style == '.') {
                    if (plus) {
                        current.style = '+';
                        additions[make_pair(x, y)] = "+ " + to_string(y + 1) + " " + to_string(x + 1);
                    } else if (star) {
                        current.style = 'x';
                        additions[make_pair(x, y)] = "x " + to_string(y + 1) + " " + to_string(x + 1);
                    }
                }
            }

            for (int j = size - 1 - m; j >= m; --j) {
                int y = size - 1 - m;
                int x = j;

                Model & current = runway[y * size + x];

                bool plus = current.style == '+' || canBePlus(mainDiagVectors[size - 1 - x + y],
                                                              offDiagVectors[(size - 1) * 2 - x - y]);

                bool star = current.style == 'x' || canBeStar(rowVectors[y], columnVectors[x]);

                if (current.style == '.') {
                    if (plus) {
                        current.style = '+';
                        additions[make_pair(x, y)] = "+ " + to_string(y + 1) + " " + to_string(x + 1);
                    } else if (star) {
                        current.style = 'x';
                        additions[make_pair(x, y)] = "x " + to_string(y + 1) + " " + to_string(x + 1);
                    }
                }
            }

            for (int j = size - 1 - m; j >= m; --j) {
                int y = j;
                int x = m;

                Model & current = runway[y * size + x];

                bool plus = current.style == '+' || canBePlus(mainDiagVectors[size - 1 - x + y],
                                                              offDiagVectors[(size - 1) * 2 - x - y]);

                bool star = current.style == 'x' || canBeStar(rowVectors[y], columnVectors[x]);

                if (current.style == '.') {
                    if (plus) {
                        current.style = '+';
                        additions[make_pair(x, y)] = "+ " + to_string(y + 1) + " " + to_string(x + 1);
                    } else if (star) {
                        current.style = 'x';
                        additions[make_pair(x, y)] = "x " + to_string(y + 1) + " " + to_string(x + 1);
                    }
                }
            }
        }

        for (int y = 0; y < size; ++y) {
            for (int x = 0; x < size; ++x) {
                Model & current = runway[y * size + x];

                bool plus = current.style == '+' || canBePlus(mainDiagVectors[size - 1 - x + y],
                                                              offDiagVectors[(size - 1) * 2 - x - y]);

                bool star = current.style == 'x' || canBeStar(rowVectors[y], columnVectors[x]);

                if (star && plus) {
                    if (current.style != 'o') {
                        current.style = 'o';
                        string addition = "o " + to_string(y + 1) + " " + to_string(x + 1);

                        additions[make_pair(x, y)] = addition;
                    }
                }

                score += current.pointValue();
            }
        }

        cout << score << " " << additions.size() << endl;

        for (auto & entry : additions) {
            cout << entry.second << endl;
        }

        delete runway;
    }

    return 0;
}