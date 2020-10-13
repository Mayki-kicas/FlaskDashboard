exec(compile(source=open('config.py').read(), filename='config.py', mode='exec'))





@app.route("/", methods=["GET"])
def main():
    cursor.execute("select Job.Id, Job.Title, Content, Company.Name, Category.Title from Job, Company, Category Where Job.Id_Company=Company.Id and Job.Id_Category=Category.Id ")
    data = cursor.fetchall()
    print(data)
    return render_template('index.html', value=data)

@app.route("/dashCategory/", methods=["GET"])
def dashCategory():
    cursor.execute("select * from Category")
    data = cursor.fetchall()
    # render templates
    return render_template('category.html', value=data)

@app.route("/dashAdvertisement/", methods=["GET"])
def dashAdvertisement():
    cursor.execute("SELECT Advertisements.Id, Advertisements.Id_User, User.Email, Advertisements.Id_Job, Job.Title FROM `Advertisements`, Job, User WHERE Job.Id=Advertisements.Id_Job and User.Id=Advertisements.Id_User Order by Id")
    data = cursor.fetchall()
    return render_template('advertisement.html', value = data)

@app.route("/dashCompany/", methods=["GET"])
def dashCompany():
    cursor.execute("SELECT * from Company")
    data = cursor.fetchall()
    return render_template('company.html', value=data)

@app.route("/dashMail", methods=["GET"])
def dashMail():
    cursor.execute("SELECT * from Mail")
    data = cursor.fetchall()
    return render_template('mail.html', value = data)

@app.route("/dashUser", methods=["GET"])
def dashUser():
    cursor.execute("SELECT * from `User`")
    data = cursor.fetchall()
    return render_template('user.html', value = data)

@app.route("/removeAdv", methods=["POST"])
def removeAdv():
    idA = request.json['id']
    if idA:
        cursor.execute('DELETE FROM Advertisements where id='+str(idA))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Advertisement deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/removeUser", methods=["POST"])
def removeUser():
    idU = request.json['id']
    if idU:
        cursor.execute("DELETE FROM User where Id="+str(idU))
        data = cursor.fetchall()
        if len(data)==0:
            conn.commit()
            return json.dumps({'message': 'User deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/removeCategory", methods=["POST"])
def removeCategory():
    idC = request.json['id']
    if idC:
        cursor.execute("DELETE FROM Category where Id="+str(idC))
        data = cursor.fetchall()
        if len(data)==0:
            conn.commit()
            return json.dumps({'message': 'Category deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/removeCompany", methods=["POST"])
def removeCompany():
    idC = request.json['id']
    if idC:
        cursor.execute("DELETE FROM Company where Id="+str(idC))
        data = cursor.fetchall()
        if len(data)==0:
            conn.commit()
            return json.dumps({'message': 'Company deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/removeMail", methods=["POST"])
def removeMail():
    idM = request.json['id']
    if idM:
        cursor.execute("DELETE FROM Mail where Id="+str(idM))
        data = cursor.fetchall()
        if len(data)==0:
            conn.commit()
            return json.dumps({'message': 'Mail deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/removeJob", methods=["POST"])
def removeJob():
    idM = request.json['id']
    if idM:
        cursor.execute("DELETE FROM Job where Id="+str(idM))
        data = cursor.fetchall()
        if len(data)==0:
            conn.commit()
            return json.dumps({'message': 'Job deleted successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/getUserUpdate<idU>", methods=["GET"])
def getUserUpdate(idU):
        cursor.execute("SELECT * from `User` where Id="+idU)
        data = cursor.fetchall()
        return render_template('update/updateUser.html', value = data)

@app.route("/updateUser", methods=["POST"])
def updateUser():
    id = request.json['id']
    name = request.json['name']
    lastname = request.json['lastname']
    age = int(request.json['age'])
    email = request.json['email']
    password = request.json['password']
    category = 0
    if name and email and password and lastname and age:
        cursor.callproc('sp_updateUser', (id, name, lastname,
                                   age, email, password, category))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'User updated successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/getCategoryUpdate<idCat>", methods=["GET"])
def getCategoryUpdate(idCat):
        cursor.execute("SELECT * from `Category` where Id="+idCat)
        data = cursor.fetchall()
        return render_template('update/updateCategory.html', value = data)

@app.route("/updateCategory", methods=["POST"])
def updateCategory():
    id = int(request.json['id'])
    title = request.json['title']
    if title:
        cursor.callproc('sp_updateCategory', (id, title))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Category updated successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/getCompanyUpdate<idComp>", methods=["GET"])
def getCompanyUpdate(idComp):
        cursor.execute("SELECT * from `Company` where Id="+idComp)
        data = cursor.fetchall()
        return render_template('update/updateCompany.html', value = data)

@app.route("/updateCompany", methods=["POST"])
def updateCompany():
    idComp = int(request.json['id'])
    name = request.json['name']
    siret = int(request.json['siret'])
    if name and siret:
        cursor.callproc('sp_updateCompany', (idComp, name, siret))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Company updated successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/getJobUpdate<idJ>", methods=["GET"])
def getJobUpdate(idJ):
        cursor.execute("SELECT * from `Job` where Id="+idJ)
        data = cursor.fetchall()
        cursor.execute("SELECT * FROM Company")
        selectComp = cursor.fetchall()
        cursor.execute("SELECT * From Category")
        selectCat = cursor.fetchall()
        return render_template('update/updateJob.html', value = data, selectComp= selectComp, selectCat= selectCat)

@app.route("/updateJob", methods=["POST"])
def updateJob():
    id = int(request.json['id'])
    title = request.json['title']
    content = request.json['content']
    id_company = int(request.json['company'])
    id_category = int(request.json['category'])

    if title and content and id_company and id_category:
        cursor.callproc('sp_updateJob', (id, title,
                                         content, id_company, id_category))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Job updated successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/getMailUpdate<idM>", methods=["GET"])
def getMailUpdate(idM):
        cursor.execute("SELECT * from `Mail` where Id="+idM)
        data = cursor.fetchall()
        return render_template('update/updateMail.html', value = data)

@app.route("/updateMail", methods=["POST"])
def updateMail():
    id = int(request.json['id'])
    content = request.json['content']
    if content:
        cursor.callproc('sp_updateMail', (id, content))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'Mail updated successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/addAdvertisement", methods=["GET", "POST"])
def addAdvertisement():
    if request.method == 'GET':
        cursor.execute("Select Id, Email From User")
        user = cursor.fetchall()
        cursor.execute("Select Id, Title from Job")
        job = cursor.fetchall()
        return render_template('add/addAdvertisement.html', user = user, job = job)
    elif request.method == "POST":
        IdUser = int(request.json['user'])
        IdJob = int(request.json['job'])
        if IdUser and IdJob:
            cursor.callproc('sp_insertAdvertisement', (IdUser, IdJob))
            data = cursor.fetchall()
            if len(data) == 0:
                conn.commit()
                return json.dumps({'message': 'Advertisement created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/addCategory", methods=["GET", "POST"])
def addCategory():
    if request.method == 'GET':
        return render_template('add/addCategory.html')
    elif request.method == 'POST':
        title = request.json['title']
        param_list = [title]
        if title:
            cursor.callproc('sp_insertCategory', (param_list))

            data = cursor.fetchall()
            if len(data) == 0:
                conn.commit()
                return json.dumps({'message': 'Category created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})

@app.route("/addCompany", methods=["GET", "POST"])
def addCompany():
    if request.method == 'GET':
        return render_template('add/addCompany.html')
    elif request.method == 'POST':
        name = request.json['name']
        siret = request.json['siret']
        if name and siret:
            cursor.callproc('sp_insertCompany', (name, siret))
            data = cursor.fetchall()
            if len(data) == 0:
                conn.commit()
                return json.dumps({'message': 'Company created successfully !'})
            else:
                return json.dumps({'error': str(data[0])})
        else:
            return json.dumps({'html': '<span>Enter the required fields</span>'})


# @app.route("/", methods=["GET", "POST"])
# def main():
#     cursor.execute("select Job.Id, Job.Title, Content, Company.Name, Category.Title from Job, Company, Category Where Job.Id_Company=Company.Id and Job.Id_Category=Category.Id ")
#     data = cursor.fetchall()
#     # render templates
#     return render_template('index.html', value=data)



@app.route('/_getInfoJob/', methods=['GET'])
def getInfoJob():
    param = request.args.get('param', 'null', type=str)
    cursor.execute("Select Company.Name, Category.Title from Job, Company, Category Where Job.Id_Company=Company.Id and Job.Id_Category=Category.Id and Job.Id="+param)
    data = cursor.fetchall()
    return jsonify(data)

@app.route("/users/<id>/", methods=['GET'])
def GetUsersId(id):
    cursor.execute("SELECT * FROM User WHERE Id="+id)
    data = cursor.fetchall()
    # render templates
    # return json.dumps(data)
    return json.dumps(data)

@app.route("/validate/", methods=['GET'])
def validate():
    _name = request.args.get('name', 'null', type=str)
    _lastname = request.args.get('lastname', 'null', type=str)
    _age = request.args.get('age', 'null', type=int)
    _category = 0
    _email = request.args.get('email', 'null', type=str)
    _password = request.args.get('password', 'null', type=str)
    _job = request.args.get('job', 'null', type=int)
    if _name and _email and _password and _lastname and _age:
        # _hashed_password = generate_password_hash(_password)
        # _hashed_password))
        # return copie of data and use sp_createUser -> create a new user in database with this information
        cursor.callproc('sp_insertUserMailAdv', (_name, _lastname, _age, _email, _password, _category, _job))
        data = cursor.fetchall()
# 0 is OK and 1 or 2 is erro
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'User created successfully ! An Email was sent to the owner of this Job.'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


@app.route('/showSignIn/', methods=['GET'])
def showSignUp():
    return render_template('registerForms.html')

# POST USER


@app.route('/signIn/', methods=['POST'])
def signIn():
    _name = request.form["inputName"]
    _lastname = request.form['inputLastName']
    _age = int(request.form['inputAge'])
    _category = request.form['inputCategory']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    # validate the received values
    if _name and _email and _password and _lastname and _age :
        # _hashed_password = generate_password_hash(_password)
        # _hashed_password))
        # return copie of data and use sp_createUser -> create a new user in database with this information
        cursor.callproc('sp_insertUser', (_name, _lastname,
                                            _age, _email, _password, _category))
        data = cursor.fetchall()
# 0 is OK and 1 or 2 is erro
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': 'User created successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})

def delete(id, table):
    if id and table:
        cursor.callproc('sp_delete'+table, (id))
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return json.dumps({'message': table+' removed successfully !'})
        else:
            return json.dumps({'error': str(data[0])})
    else:
        return json.dumps({'html': '<span>Enter the required fields</span>'})


if __name__ == "__main__":
    app.run(port=port, debug=True)
