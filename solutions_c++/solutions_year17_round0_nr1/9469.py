
#include "Round12017.h"


int Round12017::_getQtyInputLinesByTest(){
	return 1;
}

void flip(string& row, int flipperSize, int position){
	for (int i=0; i<flipperSize; i++){
		row[position + i] = (row[position + i] == '+') ? '-' : '+';
	}
}


int getCursor(string row, int flipperSize){
	int size = row.size();
	for (int i=0; i<size; i++){
		if (i + flipperSize > size){
			return size - flipperSize;
		}
		if (row[i] == '-'){
			return i;
		}
	}
	return size;
}

bool isFullyGood(string& row){
	int size = row.size();
	for (int i=0; i<size; i++){
		if (row[i] == '-'){
			return false;
		}
	}
	return true;
}

void Round12017::_calculateNextSolution(int testIndex) {

	string response = "";
	string line = this->_getParamString(testIndex, 1);
	vector<string> linePart = ShaUtilsString::split(line, " ");
	string row = linePart.at(0);
	int flipperSize = ShaUtilsConvert::toInt(linePart.at(1));

	int cursor = getCursor(row, flipperSize);
	int lastCusror;
	int qtyFlip = 0;
	while (cursor < row.size()){

		if (isFullyGood(row)){
			response = ShaUtilsConvert::toString(qtyFlip);
			break;
		}
		lastCusror = cursor;
		flip(row, flipperSize, cursor);
		qtyFlip++;
		if (isFullyGood(row)){
			response = ShaUtilsConvert::toString(qtyFlip);
			break;
		}
		cursor = getCursor(row, flipperSize);
		if (lastCusror == cursor){
			response = "IMPOSSIBLE";
			break;
		}

	}

	this->addSolution(testIndex, response);
}

