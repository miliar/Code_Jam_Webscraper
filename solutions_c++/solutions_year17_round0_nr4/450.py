#include <iostream>
#include <vector>
#include <map>

using namespace std;

struct Square {
    char model;
    map<char, bool> possibilities;

    Square() {
        model = '.';
        possibilities['+'] = true;
        possibilities['x'] = true;
        possibilities['o'] = true;
    }
};

void updateDiagonal (vector<vector<Square>>& stage, int posX, int posY, int varX, int varY, int size) {
    posX = posX + varX;
    posY = posY + varY;
    while (posX >= 0 && posX < size && posY >= 0 && posY < size) {
        stage[posX][posY].possibilities['+'] = false;
        stage[posX][posY].possibilities['o'] = false;
        posX = posX + varX;
        posY = posY + varY;
    }
}

void updateRow (vector<vector<Square>>& stage, int posX, int posY, int var, int size) {
    posX = posX + var;
    while (posX >= 0 && posX < size) {
        stage[posX][posY].possibilities['x'] = false;
        stage[posX][posY].possibilities['o'] = false;
        posX = posX + var;
    }
}

void updateColumn (vector<vector<Square>>& stage, int posX, int posY, int var, int size) {
    posY = posY + var;
    while (posY >= 0 && posY < size) {
        stage[posX][posY].possibilities['x'] = false;
        stage[posX][posY].possibilities['o'] = false;
        posY = posY + var;
    }
}

void updatePossibilities (vector<vector<Square>>& stage, int posX, int posY, int size) {
    char model = stage[posX][posY].model;

    if (model == '+') {
        updateDiagonal(stage, posX, posY, -1, -1, size);
        updateDiagonal(stage, posX, posY, +1, +1, size);
        updateDiagonal(stage, posX, posY, +1, -1, size);
        updateDiagonal(stage, posX, posY, -1, +1, size);
    }
    else if (model == 'x') {
        updateRow(stage, posX, posY, -1, size);
        updateRow(stage, posX, posY, +1, size);
        updateColumn(stage, posX, posY, -1, size);
        updateColumn(stage, posX, posY, +1, size);
    }
    else if (model == 'o') {
        updateDiagonal(stage, posX, posY, -1, -1, size);
        updateDiagonal(stage, posX, posY, +1, +1, size);
        updateDiagonal(stage, posX, posY, +1, -1, size);
        updateDiagonal(stage, posX, posY, -1, +1, size);
        updateRow(stage, posX, posY, -1, size);
        updateRow(stage, posX, posY, +1, size);
        updateColumn(stage, posX, posY, -1, size);
        updateColumn(stage, posX, posY, +1, size);
    }
}

int countPoints (vector<vector<Square>> stage, int size) {
    int points = 0;

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (stage[i][j].model == '+' || stage[i][j].model == 'x') {
                points++;
            }
            else if (stage[i][j].model == 'o') {
                points += 2;
            }
        }
    }

    return points;
}

int main () {
    int testCases;
    int size, models;
    int posX, posY;
    int modifications;
    char model;
    vector<string> answer;
    vector<vector<Square>> stage;

    cin >> testCases;
    for (int curCase = 1; curCase <= testCases; curCase++) {
        cin >> size >> models;

        stage = vector<vector<Square>>(size);
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                stage[i].push_back(Square());
            }
        }

        for (int i = 0; i < models; i++) {
            cin >> model >> posX >> posY;
            stage[posX-1][posY-1].model = model;
            stage[posX-1][posY-1].possibilities['+'] = false;
            stage[posX-1][posY-1].possibilities['x'] = false;
            if (model == 'o') {
                stage[posX-1][posY-1].possibilities['o'] = false;
            }
            updatePossibilities(stage, posX-1, posY-1, size);
        }

        modifications = 0;
        for (int i = size-1; i >= 0; i--) {
            if (stage[i][size-1].possibilities['o']) {
                modifications++;
                stage[i][size-1].model = 'o';
                answer.push_back("o " + to_string(i+1) + " " + to_string(size-1+1));
                stage[i][size-1].possibilities['+'] = false;
                stage[i][size-1].possibilities['x'] = false;
                stage[i][size-1].possibilities['o'] = false;
                updatePossibilities(stage, i, size-1, size);
            }
            else if (stage[i][size-1].possibilities['+']) {
                modifications++;
                stage[i][size-1].model = '+';
                answer.push_back("+ " + to_string(i+1) + " " + to_string(size-1+1));
                stage[i][size-1].possibilities['+'] = false;
                stage[i][size-1].possibilities['x'] = false;
                stage[i][size-1].possibilities['o'] = false;
                updatePossibilities(stage, i, size-1, size);
            }
            else if (stage[i][size-1].possibilities['x']) {
                modifications++;
                stage[i][size-1].model = 'x';
                answer.push_back("x " + to_string(i+1) + " " + to_string(size-1+1));
                stage[i][size-1].possibilities['+'] = false;
                stage[i][size-1].possibilities['x'] = false;
                stage[i][size-1].possibilities['o'] = false;
                updatePossibilities(stage, i, size-1, size);
            }
        }

        for (int i = size-1; i >= 0; i--) {
            if (stage[i][0].possibilities['o']) {
                modifications++;
                stage[i][0].model = 'o';
                answer.push_back("o " + to_string(i+1) + " " + to_string(0+1));
                stage[i][0].possibilities['+'] = false;
                stage[i][0].possibilities['x'] = false;
                stage[i][0].possibilities['o'] = false;
                updatePossibilities(stage, i, 0, size);
            }
            else if (stage[i][0].possibilities['+']) {
                modifications++;
                stage[i][0].model = '+';
                answer.push_back("+ " + to_string(i+1) + " " + to_string(0+1));
                stage[i][0].possibilities['+'] = false;
                stage[i][0].possibilities['x'] = false;
                stage[i][0].possibilities['o'] = false;
                updatePossibilities(stage, i, 0, size);
            }
            else if (stage[i][0].possibilities['x']) {
                modifications++;
                stage[i][0].model = 'x';
                answer.push_back("x " + to_string(i+1) + " " + to_string(0+1));
                stage[i][0].possibilities['+'] = false;
                stage[i][0].possibilities['x'] = false;
                stage[i][0].possibilities['o'] = false;
                updatePossibilities(stage, i, 0, size);
            }
        }

        for (int i = size-1; i >= 0; i--) {
            for (int j = size-1; j >= 0; j--) {
                if (stage[i][j].possibilities['o']) {
                    modifications++;
                    stage[i][j].model = 'o';
                    answer.push_back("o " + to_string(i+1) + " " + to_string(j+1));
                    stage[i][j].possibilities['+'] = false;
                    stage[i][j].possibilities['x'] = false;
                    stage[i][j].possibilities['o'] = false;
                    updatePossibilities(stage, i, j, size);
                }
                else if (stage[i][j].possibilities['+']) {
                    modifications++;
                    stage[i][j].model = '+';
                    answer.push_back("+ " + to_string(i+1) + " " + to_string(j+1));
                    stage[i][j].possibilities['+'] = false;
                    stage[i][j].possibilities['x'] = false;
                    stage[i][j].possibilities['o'] = false;
                    updatePossibilities(stage, i, j, size);
                }
                else if (stage[i][j].possibilities['x']) {
                    modifications++;
                    stage[i][j].model = 'x';
                    answer.push_back("x " + to_string(i+1) + " " + to_string(j+1));
                    stage[i][j].possibilities['+'] = false;
                    stage[i][j].possibilities['x'] = false;
                    stage[i][j].possibilities['o'] = false;
                    updatePossibilities(stage, i, j, size);
                }
            }
        }

        cout << "Case #" << curCase << ": " << countPoints(stage, size) << " " << modifications << endl;
        for (vector<string>::iterator it = answer.begin(); it < answer.end(); it++) {
            cout << *it << endl;
        }

        /*
        //DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                cout << stage[i][j].model;
            }
            cout << endl;
        }
        cout << endl;
        //DEBUG DEBUG DEBUG DEBUG DEBUG DEBUG
        */

        answer.clear();
    }

    return 0;
}